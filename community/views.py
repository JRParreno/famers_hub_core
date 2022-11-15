from django.shortcuts import render
from rest_framework import generics, permissions, response, status

from core.paginate import ExtraSmallResultsSetPagination
from .models import Post
from .serializers import PostSerializer, PostCreateSerializer
# , PostUpdateSerializer

# Create your views here.


class PostListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-date_updated')
    pagination_class = ExtraSmallResultsSetPagination


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostCreateSerializer
