from rest_framework import serializers
from .models import UserProfile
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'pk',
            'email',
            'first_name',
            'last_name',
            'username',
            'get_full_name'
        )

        extra_kwargs = {
            'username': {
                'read_only': True
            },
        }


class AuthorSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = UserProfile
        fields = ['pk', 'user', 'profile_photo']
