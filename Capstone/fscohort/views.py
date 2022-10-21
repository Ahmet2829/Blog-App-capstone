from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView

# Create your views here.
from .models import (
    Post,
    PostView,
    Like,
    Comment
)
from .serializers import (
    PostSerializer,
    PostViewSerializer,
    LikeSerializer,
    CommentSerializer
)


class PostViews(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    # def perform_update(self, serializer):
    #     instance = self.get_object()  # instance before update
    #     self.request.data.get("title", None)  # read data from request
    #     if self.request.user.is_authenticated:
    #         updated_instance = serializer.save(author=self.request.user)
    #     else:
    #         updated_instance = serializer.save()


class PostView_View(viewsets.ModelViewSet):
    queryset = PostView.objects.all()
    serializer_class = PostViewSerializer


class CommentView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LikesView(viewsets.ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)


