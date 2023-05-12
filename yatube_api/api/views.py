from django.shortcuts import get_object_or_404
from django.core.exceptions import PermissionDenied
from rest_framework import mixins, permissions
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import (ModelViewSet, ReadOnlyModelViewSet,
                                     GenericViewSet)
from posts.models import Follow, Group, Post, User, Comment
from .permissions import OwnerOrReadOnly
from .serializers import (CommentSerializer, FollowSerializer, GroupSerializer,
                          PostSerializer, UserSerializer)


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (OwnerOrReadOnly,)

    def get_queryset(self):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        return post.comments

    def perform_create(self, serializer):
        post = get_object_or_404(Post, pk=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Вы не можете изменить чужой комментарий.')
        super(CommentViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Вы не можете удалить чужой комментарий.')
        super(CommentViewSet, self).perform_destroy(serializer)


class GroupViewSet(ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (OwnerOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise PermissionDenied('Вы не можете изменить чужой пост.')
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise PermissionDenied('Вы не можете удалить чужой пост.')
        super(PostViewSet, self).perform_destroy(serializer)


class UserViewSet(ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class FollowViewSet(mixins.CreateModelMixin,
                    mixins.ListModelMixin,
                    GenericViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    filter_backends = (SearchFilter,)
    search_fields = ('following__username', 'user__username',)

    def get_queryset(self):
        new_queryset = Follow.objects.filter(user=self.request.user)
        return new_queryset

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)
