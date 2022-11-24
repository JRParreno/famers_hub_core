from rest_framework import generics, permissions, response, status, parsers
from core.utils import check_photo_url

from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string
from django.contrib.auth.models import User

from .serializers import (AuthorSerializer,)
from .models import UserProfile


class UserProfileView(generics.RetrieveUpdateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = AuthorSerializer

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({
            'request': self.request
        })
        return context

    def get(self, request, *args, **kwargs):
        user = self.request.user
        user_profiles = UserProfile.objects.filter(user=user)
        if user_profiles.exists():
            user_profile = user_profiles.first()
            data = {
                "pk": user_profile.pk,
                "username": user.username,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "email": user.email,
                "profile_photo": check_photo_url(user_profile.profile_photo),
                "mobile_number": user.username,
            }

            return response.Response(data, status=status.HTTP_200_OK)

        else:
            error = {
                "error_message": "Please setup your profile"
            }
            return response.Response(error, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, *args, **kwargs):
        user = self.request.user
        user_details = self.request.data.get('user')
        mobile_number = self.request.data.get('mobile_number')
        email = UserProfile.objects.filter(
            user__email=user_details['email']).exclude(user=user).exists()
        check_mobile_number = UserProfile.objects.filter(
            user__username=mobile_number).exclude(user=user).exists()

        if email:
            error = {
                "error_message": "Email already exists"
            }
            return response.Response(error, status=status.HTTP_400_BAD_REQUEST)

        if check_mobile_number:
            error = {
                "error_message": "Mobile number already exists"
            }
            return response.Response(error, status=status.HTTP_400_BAD_REQUEST)

        user_profile = UserProfile.objects.get(user=user)

        user.email = user_details['email']
        user.first_name = user_details['first_name']
        user.last_name = user_details['last_name']
        user.username = mobile_number
        user.save()

        data = {
            "pk": user_profile.pk,
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email,
            "profile_photo": check_photo_url(user_profile.profile_photo),
            "mobile_number": user.username,
        }

        return response.Response(data, status=status.HTTP_200_OK)
