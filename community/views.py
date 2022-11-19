from django.shortcuts import render
from rest_framework import generics, permissions, response, status, exceptions

from core.paginate import ExtraSmallResultsSetPagination
from .models import Post, Comment
from .serializers import PostSerializer, PostCreateSerializer, CommentSerializer
# , PostUpdateSerializer


class PostListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-date_updated')
    pagination_class = ExtraSmallResultsSetPagination


class PostDetailView(generics.RetrieveAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostSerializer
    queryset = Post.objects.all().order_by('-date_updated')


class PostCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = PostCreateSerializer


class CommentCreateView(generics.CreateAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer


class CommentListView(generics.ListAPIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CommentSerializer
    queryset = Comment.objects.all().order_by('-date_updated')
    pagination_class = ExtraSmallResultsSetPagination

    def get_queryset(self):
        post = self.request.query_params.get('post', None)

        check_post = Post.objects.filter(pk=post)

        if check_post.exists():

            comments = Comment.objects.filter(
                post__pk=post).order_by('-date_updated')
            return comments
        else:
            error = {
                "error_message": "Post not found"
            }
        raise exceptions.ValidationError(
            detail=error, code=status.HTTP_400_BAD_REQUEST)
