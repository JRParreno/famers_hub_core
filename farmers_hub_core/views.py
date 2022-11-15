import json
from django.shortcuts import render
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.debug import sensitive_post_parameters
from oauth2_provider.models import get_access_token_model
from oauth2_provider.signals import app_authorized
from oauth2_provider.views.base import TokenView
from farmers_hub_core.serializers import RegisterSerializer
from user_profile.models import UserProfile
from rest_framework import generics, permissions, response, status
from django.contrib.auth.models import User
from django.conf import settings
from oauth2_provider.models import (
    Application,
    RefreshToken,
    AccessToken
)
from datetime import (
    datetime,
    timedelta
)
from django.shortcuts import get_object_or_404
from django.utils.crypto import get_random_string


class TokenViewWithUserId(TokenView):
    @method_decorator(sensitive_post_parameters("password"))
    def post(self, request, *args, **kwargs):
        url, headers, body, status = self.create_token_response(request)
        print(body)

        if status == 200:
            body = json.loads(body)
            access_token = body.get("access_token")
            if access_token is not None:
                token = get_access_token_model().objects.get(
                    token=access_token)
                app_authorized.send(
                    sender=self, request=request,
                    token=token)
                body['id'] = str(token.user.id)
                body = json.dumps(body)
        response = HttpResponse(content=body, status=status)
        for k, v in headers.items():
            response[k] = v
        return response


class RegisterView(generics.CreateAPIView):
    permission_classes = []
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create_access_token(self, user):
        application = Application.objects.all()

        if application.exists():
            self.expire_seconds = settings.OAUTH2_PROVIDER['ACCESS_TOKEN_EXPIRE_SECONDS']
            scopes = settings.OAUTH2_PROVIDER['SCOPES']
            expires = datetime.now() + timedelta(seconds=self.expire_seconds)
            token = get_random_string(32)
            refresh_token = get_random_string(32)

            access_token = AccessToken.objects.create(
                user=user,
                expires=expires,
                scope=scopes,
                token=token,
                application=application.first(),
            )

            refresh_token = RefreshToken.objects.create(
                user=user,
                access_token=access_token,
                token=refresh_token,
                application=application.first(),
            )

            return access_token, refresh_token

        return None

    def post(self, request, *args, **kwargs):
        password = request.data.get('password')
        confirm_password = request.data.get('confirm_password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        mobile_number = request.data.get('mobile_number')

        email = request.data.get('email')

        if User.objects.filter(username=mobile_number).exists():
            data = {
                "error_message": "Mobile number Already exists"
            }
            return response.Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )

        if User.objects.filter(email=email).exists():
            data = {
                "error_message": "Email Already exists"
            }
            return response.Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )

        if password != confirm_password:
            data = {
                "error_message": "Password does not match"
            }
            return response.Response(
                data=data,
                status=status.HTTP_400_BAD_REQUEST
            )

        user = User.objects.create(
            username=mobile_number, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.save()

        UserProfile.objects.create(user=user,)

        oauth_token, refresh_token = self.create_access_token(
            user)

        data = {
            "access_token": oauth_token.token,
            "expires": self.expire_seconds,
            "token_type": "Bearer",
            "scope": oauth_token.scope,
            "refresh_token": refresh_token.token
        }

        return response.Response(
            data=data,
            status=status.HTTP_200_OK
        )


def home(request):
    return render(request, 'home.html',)


def about(request):

    return render(request, 'about.html',)


def contact(request):

    return render(request, 'contact.html',)
