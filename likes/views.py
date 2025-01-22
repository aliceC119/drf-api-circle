from rest_framework import generics, permissions
from drf_api.permissions import IsOwnerOrReadOnly
from likes.models import Like, Post, VideoPost
from likes.serializers import LikeSerializer


class LikePost(generics.ListCreateAPIView):
    """
    List likes or create a like if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        post_id = self.kwargs['pk']
        post = Post.objects.get(pk=post_id)
        serializer.save(owner=self.request.user)


class LikePostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

class LikeVideoPost(generics.CreateAPIView):
    """
    Like a video post if logged in.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()

    def perform_create(self, serializer):
        video_post_id = self.kwargs['pk']
        video_post = VideoPost.objects.get(pk=video_post_id)
        serializer.save(owner=self.request.user, video_post=video_post)

class LikeVideoPostDetail(generics.RetrieveDestroyAPIView):
    """
    Retrieve a like or delete it by id if you own it.
    """
    permission_classes = [IsOwnerOrReadOnly]
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
#class VideoPostLikeList(generics.ListCreateAPIView):
#   """
#   List likes or create a like if logged in.
#   """
#   permission_classes = [permissions.IsAuthenticatedOrReadOnly]
#   serializer_class = VideoPostLikeSerializer
#   queryset = VideoPostLike.objects.all()

#   def perform_create(self, serializer):
#       serializer.save(owner=self.request.user)


#class VideoPostLikeDetail(generics.RetrieveDestroyAPIView):
#   """
#   Retrieve a like or delete it by id if you own it.
#   """
#   permission_classes = [IsOwnerOrReadOnly]
#   serializer_class = VideoPostLikeSerializer
#   queryset = VideoPostLike.objects.all()