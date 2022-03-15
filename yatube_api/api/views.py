from django.shortcuts import get_object_or_404
from django.utils.functional import cached_property
from posts.models import Follow, Group, Post, User
from rest_framework import permissions, viewsets
from rest_framework.pagination import LimitOffsetPagination

from .permissions import AuthorOrReadOnly
from .serializers import (
    CommentSerializer,
    FollowSerializer,
    GroupSerializer,
    PostSerializer,
)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)

    @cached_property
    def comment_post(self):
        post = get_object_or_404(Post, pk=self.kwargs['post_id'])
        return post

    def get_queryset(self):
        self.comment_post.comments.all()
        return self.comment_post.comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.comment_post)


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    queryset = Follow.objects.all()


class FollowViewSet(viewsets.ModelViewSet):

    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_queryset(self):
        return Follow.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
