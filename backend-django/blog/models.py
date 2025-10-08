from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# User model
class Users(AbstractUser): 
    username = models.CharField(max_length=255, unique=True)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=255)
    avatar = models.ImageField(upload_to="avatars/", blank=True, null=True)
    password_reset_token = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.email
    
# Post model
class Posts(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(max_length=1000)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title


