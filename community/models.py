from django.db import models
from django.contrib.auth.models import User
from user_profile.models import UserProfile


class Post(models.Model):
    profile = models.ForeignKey(
        UserProfile, related_name='post_user', on_delete=models.CASCADE)

    description = models.TextField(blank=False, null=False)
    image = models.ImageField(
        upload_to='images/post/', blank=True, null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.description


class Comment(models.Model):
    post = models.ForeignKey(
        Post, related_name='post_comment_user', on_delete=models.CASCADE)
    profile = models.ForeignKey(
        UserProfile, related_name='comment_user', on_delete=models.CASCADE)
    description = models.TextField(blank=False, null=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f'{self.description}'
