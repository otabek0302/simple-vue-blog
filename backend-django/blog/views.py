from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import generics
from django.core.mail import send_mail
from .models import Users
from .serializers import (
    RegisterSerializer,
    LoginSerializer,
    ForgotPasswordSerializer,
    ResetPasswordSerializer,
)
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
                f"Click the link to reset your password: http://localhost:3000/reset-password?token={password_reset_token}",
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
