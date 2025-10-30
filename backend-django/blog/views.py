from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.core.mail import send_mail
from django.db.models import Q
from django.core.files.storage import default_storage
from .models import Users, Posts, PostLike, PostComment
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
    UpdateProfileSerializer,
    ChangePasswordSerializer,
    PostSerializer,
    CreatePostSerializer,
    UpdatePostSerializer,
    CommentSerializer,
    UpdateAvatarSerializer,
)
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from rest_framework.exceptions import ValidationError
import uuid


# Registration views
class RegistrationViewSet(generics.CreateAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Validate data
        username = serializer.validated_data["username"]
        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        if Users.objects.filter(email=email).exists():
            return Response(
                {"error": True, "message": "Email already exists"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user = Users(username=username, email=email)
        user.set_password(password)
        user.save()

        refresh = RefreshToken.for_user(user)
        tokens = {"refresh": str(refresh), "access": str(refresh.access_token)}

        return Response(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "avatar": user.avatar.url if user.avatar else None,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
                "tokens": tokens,
                "message": "User registered successfully !",
            },
            status=status.HTTP_201_CREATED,
        )


# Login views
class LoginView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]
        password = serializer.validated_data["password"]

        user = Users.objects.filter(email=email).first()
        if not user:
            return Response(
                {"error": True, "message": "User with this email not found !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        if not user.check_password(password):
            return Response(
                {"error": True, "message": "Password is incorrect !"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        refresh = RefreshToken.for_user(user)
        tokens = {"refresh": str(refresh), "access": str(refresh.access_token)}

        return Response(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "avatar": user.avatar.url if user.avatar else None,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
                "tokens": tokens,
                "message": "Login successful !",
            },
            status=status.HTTP_200_OK,
        )


# Forgot password views
class ForgotPasswordView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ForgotPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data["email"]

        try:
            user = Users.objects.get(email=email)
        except Users.DoesNotExist:
            return Response(
                {"error": True, "message": "User not found with this email"},
                status=status.HTTP_404_NOT_FOUND,
            )

        # Generate password reset token
        password_reset_token = str(uuid.uuid4())
        user.password_reset_token = password_reset_token
        user.save()

        try:
            # Send email to user
            send_mail(
                "Password Reset Request",
                f"Click the link to reset your password: http://localhost:5173/reset-password?token={password_reset_token}",
                "noreply@example.com",
                [email],
                fail_silently=False,
            )

            return Response(
                {"message": f"Password reset email sent successfully to {email}!"},
                status=status.HTTP_200_OK,
            )
        except Exception:
            # Clear the token if email sending fails
            user.password_reset_token = None
            user.save()

            return Response(
                {"error": True, "message": "Failed to send email. Please try again."},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )


# Reset password views
class ResetPasswordView(generics.GenericAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        token = serializer.validated_data["token"]
        password = serializer.validated_data["password"]

        try:
            user = Users.objects.get(password_reset_token=token)
        except Users.DoesNotExist:
            return Response(
                {"error": True, "message": "Invalid or expired reset token"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        # Update password and clear reset token
        user.set_password(password)
        user.password_reset_token = None
        user.save()

        return Response(
            {"message": "Password reset successfully!"},
            status=status.HTTP_200_OK,
        )


class UpdateProfileView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UpdateProfileSerializer

    def put(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response(
                {"error": True, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        new_username = serializer.validated_data["username"]
        new_email = serializer.validated_data["email"]

        # Uniqueness checks
        if Users.objects.exclude(id=user.id).filter(email=new_email).exists():
            return Response(
                {"error": True, "message": "Email already taken"},
                status=status.HTTP_400_BAD_REQUEST,
            )

        user.username = new_username
        user.email = new_email
        user.save()

        return Response(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "avatar": user.avatar.url if user.avatar else None,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
                "message": "Profile updated successfully",
            },
            status=status.HTTP_200_OK,
        )


class ChangePasswordView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = ChangePasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        password = serializer.validated_data["password"]

        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response(
                {"error": True, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        user.set_password(password)
        user.save()

        return Response(
            {"message": "Password updated successfully"},
            status=status.HTTP_200_OK,
        )


class UpdateAvatarView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    serializer_class = UpdateAvatarSerializer
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        try:
            user = Users.objects.get(id=request.user.id)
        except Users.DoesNotExist:
            return Response(
                {"error": True, "message": "User not found"},
                status=status.HTTP_404_NOT_FOUND,
            )

        if serializer.validated_data.get("remove"):
            if user.avatar:
                # Delete the file from storage
                old_avatar_name = user.avatar.name
                user.avatar.delete(save=False)
                if old_avatar_name:
                    try:
                        if default_storage.exists(old_avatar_name):
                            default_storage.delete(old_avatar_name)
                    except Exception:
                        pass
            user.avatar = None
        else:
            avatar_file = serializer.validated_data.get("avatar")
            if not avatar_file:
                return Response(
                    {"error": True, "message": "Avatar file is required"},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            # Delete old avatar if exists
            if user.avatar:
                old_avatar_name = user.avatar.name
                user.avatar.delete(save=False)
                if old_avatar_name:
                    try:
                        if default_storage.exists(old_avatar_name):
                            default_storage.delete(old_avatar_name)
                    except Exception:
                        pass
            user.avatar = avatar_file
        user.save()

        return Response(
            {
                "user": {
                    "id": user.id,
                    "username": user.username,
                    "email": user.email,
                    "avatar": user.avatar.url if user.avatar else None,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at,
                },
                "message": "Avatar updated successfully",
            },
            status=status.HTTP_200_OK,
        )


class MyPostsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.filter(author=request.user)

        # Handle search query
        search_query = request.query_params.get("search", "").strip()
        if search_query:
            posts = posts.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        posts = posts.order_by("-created_at")
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)


class LikedPostsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        # Get posts that the current user has liked
        liked_posts = Posts.objects.filter(likes__user=request.user).distinct()

        # Handle search query
        search_query = request.query_params.get("search", "").strip()
        if search_query:
            from django.db.models import Q

            liked_posts = liked_posts.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        liked_posts = liked_posts.order_by("-created_at")
        serializer = PostSerializer(
            liked_posts, many=True, context={"request": request}
        )
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)


class PostsListCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser]

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.all()

        # Handle search query
        search_query = request.query_params.get("search", "").strip()
        if search_query:
            posts = posts.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        posts = posts.order_by("-created_at")
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        try:
            serializer = CreatePostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)

            image_file = serializer.validated_data.get("image")
            post = Posts.objects.create(
                title=serializer.validated_data["title"],
                content=serializer.validated_data["content"],
                image=image_file,
                author=request.user,
            )
            return Response(
                PostSerializer(post, context={"request": request}).data,
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as exc:
            return Response(
                {"error": True, "errors": exc.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exc:
            return Response(
                {"error": True, "message": str(exc)}, status=status.HTTP_400_BAD_REQUEST
            )


class PostsOthersListView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, *args, **kwargs):
        posts = Posts.objects.exclude(author=request.user)

        # Handle search query
        search_query = request.query_params.get("search", "").strip()
        if search_query:
            posts = posts.filter(
                Q(title__icontains=search_query) | Q(content__icontains=search_query)
            )

        posts = posts.order_by("-created_at")
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)


class PostDetailUpdateDeleteView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    parser_classes = [MultiPartParser, FormParser, JSONParser]

    def get_object(self, pk):
        try:
            return Posts.objects.get(pk=pk)
        except Posts.DoesNotExist:
            return None

    def get(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(
            PostSerializer(post, context={"request": request}).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if post.author_id != request.user.id:
            return Response(
                {"error": True, "message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )

        try:
            serializer = UpdatePostSerializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            post.title = serializer.validated_data["title"]
            post.content = serializer.validated_data["content"]

            # Handle image removal
            if serializer.validated_data.get("removeImage", False):
                if post.image:
                    # Delete the file from storage
                    old_image_name = post.image.name
                    post.image.delete(save=False)
                    if old_image_name:
                        try:
                            if default_storage.exists(old_image_name):
                                default_storage.delete(old_image_name)
                        except Exception:
                            pass
                post.image = None
            elif (
                "image" in serializer.validated_data
                and serializer.validated_data["image"]
            ):
                # Delete old image if exists
                if post.image:
                    old_image_name = post.image.name
                    post.image.delete(save=False)
                    if old_image_name:
                        try:
                            if default_storage.exists(old_image_name):
                                default_storage.delete(old_image_name)
                        except Exception:
                            pass
                post.image = serializer.validated_data["image"]

            post.save()
            return Response(
                PostSerializer(post, context={"request": request}).data,
                status=status.HTTP_200_OK,
            )
        except ValidationError as exc:
            return Response(
                {"error": True, "errors": exc.detail},
                status=status.HTTP_400_BAD_REQUEST,
            )
        except Exception as exc:
            return Response(
                {"error": True, "message": str(exc)}, status=status.HTTP_400_BAD_REQUEST
            )

    def delete(self, request, pk, *args, **kwargs):
        post = self.get_object(pk)
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if post.author_id != request.user.id:
            return Response(
                {"error": True, "message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )

        # Delete the post image file if it exists
        if post.image:
            image_name = post.image.name
            post.image.delete(save=False)
            if image_name:
                try:
                    if default_storage.exists(image_name):
                        default_storage.delete(image_name)
                except Exception:
                    pass

        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk, *args, **kwargs):
        post = Posts.objects.filter(pk=pk).first()
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        PostLike.objects.get_or_create(post=post, user=request.user)
        # Return updated post data
        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def post(self, request, pk, *args, **kwargs):
        post = Posts.objects.filter(pk=pk).first()
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        PostLike.objects.filter(post=post, user=request.user).delete()
        # Return updated post data
        serializer = PostSerializer(post, context={"request": request})
        return Response(serializer.data, status=status.HTTP_200_OK)


class PostCommentsListCreateView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, post_pk, *args, **kwargs):
        post = Posts.objects.filter(pk=post_pk).first()
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        comments = PostComment.objects.filter(post=post).order_by("created_at")
        return Response(
            {"results": CommentSerializer(comments, many=True).data},
            status=status.HTTP_200_OK,
        )

    def post(self, request, post_pk, *args, **kwargs):
        post = Posts.objects.filter(pk=post_pk).first()
        if not post:
            return Response(
                {"error": True, "message": "Post not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        comment_text = request.data.get("comment", "").strip()
        if not comment_text:
            return Response(
                {"error": True, "message": "Comment is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        comment = PostComment.objects.create(
            post=post, user=request.user, comment=comment_text
        )
        return Response(CommentSerializer(comment).data, status=status.HTTP_201_CREATED)


class PostCommentDetailView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def put(self, request, pk, *args, **kwargs):
        comment = PostComment.objects.filter(pk=pk).first()
        if not comment:
            return Response(
                {"error": True, "message": "Comment not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if comment.user_id != request.user.id:
            return Response(
                {"error": True, "message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )
        text = request.data.get("comment", "").strip()
        if not text:
            return Response(
                {"error": True, "message": "Comment is required"},
                status=status.HTTP_400_BAD_REQUEST,
            )
        comment.comment = text
        comment.save()
        return Response(CommentSerializer(comment).data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        comment = PostComment.objects.filter(pk=pk).first()
        if not comment:
            return Response(
                {"error": True, "message": "Comment not found"},
                status=status.HTTP_404_NOT_FOUND,
            )
        if comment.user_id != request.user.id:
            return Response(
                {"error": True, "message": "Forbidden"},
                status=status.HTTP_403_FORBIDDEN,
            )
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserPostsView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [JWTAuthentication]

    def get(self, request, user_pk, *args, **kwargs):
        posts = Posts.objects.filter(author_id=user_pk).order_by("-created_at")
        serializer = PostSerializer(posts, many=True, context={"request": request})
        return Response({"results": serializer.data}, status=status.HTTP_200_OK)
