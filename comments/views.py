from rest_framework import generics, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from drf_api.permissions import IsOwnerOrReadOnly
from .models import Comment, VideoPostComment
from .serializers import CommentSerializer, CommentDetailSerializer, VideoPostCommentSerializer, VideoPostCommentDetailSerializer



class CommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Comment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['post',]

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = CommentDetailSerializer
    queryset = Comment.objects.all()

class VideoPostCommentList(generics.ListCreateAPIView):
    """
    List comments or create a comment if logged in.
    """
    serializer_class = VideoPostCommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = VideoPostComment.objects.all()

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['video_post']

    def perform_create(self, serializer):
       serializer.save(owner=self.request.user)


class VideoPostCommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve a comment, or update or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = VideoPostCommentDetailSerializer
    queryset = VideoPostComment.objects.all()

