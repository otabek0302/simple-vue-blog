from rest_framework import serializers
from .models import Posts, PostComment, PostLike


# Registration serializers
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].validators = []
        self.fields["email"].validators = []
        self.fields["password"].validators = []


# Login serializers
class LoginSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].validators = []
        self.fields["password"].validators = []


# Forgot password serializers
class ForgotPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["email"].validators = []


# Reset password serializers
class ResetPasswordSerializer(serializers.Serializer):
    token = serializers.CharField(max_length=255)
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["token"].validators = []
        self.fields["password"].validators = []


# Update profile serializers
class UpdateProfileSerializer(serializers.Serializer):
    username = serializers.CharField(max_length=255)
    email = serializers.EmailField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["username"].validators = []
        self.fields["email"].validators = []


# Change password serializers
class ChangePasswordSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].validators = []

# Update avatar serializers
class UpdateAvatarSerializer(serializers.Serializer):
    avatar = serializers.ImageField(required=False, allow_null=True)
    remove = serializers.BooleanField(required=False, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["avatar"].validators = []

# Delete account serializers
class DeleteAccountSerializer(serializers.Serializer):
    password = serializers.CharField(write_only=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["password"].validators = []

# Get profile serializers
class GetProfileSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_id"].validators = []

# Post serializers
class CreatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=1000)
    image = serializers.ImageField(required=False, allow_null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].validators = []
        self.fields["content"].validators = []
        self.fields["image"].validators = []

# Update post serializers
class UpdatePostSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(max_length=1000)
    image = serializers.ImageField(required=False, allow_null=True)
    removeImage = serializers.BooleanField(required=False, default=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].validators = []
        self.fields["content"].validators = []
        self.fields["image"].validators = []

# Delete post serializers
class DeletePostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["post_id"].validators = []

# Like post serializers
class LikePostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["post_id"].validators = []

# Unlike post serializers
class UnlikePostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["post_id"].validators = []

# Comment post serializers
class CommentPostSerializer(serializers.Serializer):
    post_id = serializers.IntegerField()
    comment = serializers.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["post_id"].validators = []
        self.fields["comment"].validators = []

# Update comment serializers
class UpdateCommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()
    comment = serializers.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["comment_id"].validators = []
        self.fields["comment"].validators = []

# Delete comment serializers
class DeleteCommentSerializer(serializers.Serializer):
    comment_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)   
        self.fields["comment_id"].validators = []

# Get liked posts serializers
class GetLikedPostsSerializer(serializers.Serializer):
    user_id = serializers.IntegerField()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["user_id"].validators = []


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SerializerMethodField()
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()

    class Meta:
        model = Posts
        fields = [
            "id",
            "title",
            "content",
            "image",
            "author",
            "likes_count",
            "comments_count",
            "is_liked",
            "created_at",
            "updated_at",
        ]

    def get_author(self, obj):
        user = obj.author
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "avatar": user.avatar.url if user.avatar else None,
        }

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_is_liked(self, obj):
        request = self.context.get("request")
        if request and request.user.is_authenticated:
            return obj.likes.filter(user=request.user).exists()
        return False


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.SerializerMethodField()

    class Meta:
        model = PostComment
        fields = [
            "id",
            "post_id",
            "comment",
            "user",
            "created_at",
            "updated_at",
        ]

    def get_user(self, obj):
        user = obj.user
        return {
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "avatar": user.avatar.url if user.avatar else None,
        }