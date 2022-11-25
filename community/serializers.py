from rest_framework import serializers
from user_profile.models import UserProfile
from user_profile.serializers import AuthorSerializer
from community.models import Post, Comment
import base64
from core.utils import get_random_code
from django.core.files.base import ContentFile


class CommentSerializer(serializers.ModelSerializer):
    profile = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = ('pk', 'post', 'profile',
                  'description', 'date_created',
                  'date_updated'
                  )

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(CommentSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        current_user = self.request.user
        description = validated_data.pop('description')
        post = validated_data.pop('post')
        users_profile = UserProfile.objects.get(user=current_user)

        comment_instance = Comment.objects.create(
            post=post, description=description, profile=users_profile)

        comment_instance.save()

        return comment_instance


class PostSerializer(serializers.ModelSerializer):
    profile = AuthorSerializer(read_only=True)

    class Meta:
        model = Post
        fields = ('pk', 'profile',
                  'description', 'image', 'date_created',
                  'date_updated'
                  )

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(PostSerializer, self).__init__(*args, **kwargs)

    def to_representation(self, instance):
        data = super(PostSerializer, self).to_representation(instance)
        if 'request' in self.context and self.request:
            commment_total = Comment.objects.filter(post=data['pk']).count()
            data['comment_total'] = commment_total
        return data


class PostCreateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(
        allow_null=False, required=True)

    class Meta:
        model = Post
        fields = ('pk', 'description', 'image')

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(PostCreateSerializer, self).__init__(*args, **kwargs)

    def create(self, validated_data):
        current_user = self.request.user
        users_profile = UserProfile.objects.get(user=current_user)

        def extract_file(base64_string, image_type):
            img_format, img_str = base64_string.split(';base64,')
            ext = img_format.split('/')[-1]
            return f"post-image-{get_random_code()}-{image_type}.{ext}", ContentFile(base64.b64decode(img_str))

        image = validated_data.pop('image', None)

        description = validated_data.pop('description')
        post_instance = Post.objects.create(
            profile=users_profile, description=description)

        if image:
            filename, data = extract_file(
                image, 'image')
            post_instance.image.save(filename, data, save=True)

        post_instance.save()

        return post_instance


class PostUpdateSerializer(serializers.ModelSerializer):
    image = serializers.CharField(
        allow_null=False, required=True)

    class Meta:
        model = Post
        fields = ('pk', 'description', 'image')

    def __init__(self, *args, **kwargs):
        # init context and request
        context = kwargs.get('context', {})
        self.request = context.get('request', None)
        self.kwargs = context.get("kwargs", None)

        super(PostUpdateSerializer, self).__init__(*args, **kwargs)

    def update(self, instance, validated_data):
        current_user = self.request.user
        users_profile = UserProfile.objects.get(user=current_user)

        def extract_file(base64_string, image_type):
            img_format, img_str = base64_string.split(';base64,')
            ext = img_format.split('/')[-1]
            return f"post-image-{get_random_code()}-{image_type}.{ext}", ContentFile(base64.b64decode(img_str))

        image = validated_data.pop('image', None)
        pk = validated_data.pop('pk', None)

        description = validated_data.pop('description')
        instance.description = description

        if image:
            filename, data = extract_file(
                image, 'image')
            instance.image.save(filename, data, save=True)

        instance.save()

        return instance
