from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    class ProfileManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().select_related('user')
    
    user = models.OneToOneField(
        User, related_name='profile', on_delete=models.CASCADE)
    profile_photo = models.ImageField(
        upload_to='profile-photo/', blank=True, null=True)


    def __str__(self):
        return f'{self.user.last_name} - {self.user.first_name}'