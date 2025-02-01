from django.urls import path
from likes import views  

urlpatterns = [
    
    path('likes/posts/', views.LikePost.as_view(), name='post-like-list'),  # List all post likes
    path('likes/posts/<int:pk>/', views.LikePost.as_view(), name='like-post'),
    path('likes/videoposts/', views.VideoPostLikeList.as_view(), name='video-post-like-list'),  # List all video post likes
    path('likes/videoposts/<int:pk>/', views.VideoPostLikeDetail.as_view(), name='like-video-post'),
    
]
