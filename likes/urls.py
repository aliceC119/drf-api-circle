from django.urls import path
from likes import views  

urlpatterns = [
    
    path('likes/posts/', views.LikePost.as_view(), name='post-like-list'),  # List all post likes
    #path('likes/posts/<int:pk>', views.LikePost.as_view(), name='like-post'),
    #path('likes/<int:pk>/detail/', views.LikePostDetail.as_view(), name='like-post-detail'),
    path('likes/videoposts/', views.LikeVideoPost.as_view(), name='video-post-like-list'),  # List all video post likes
    #path('likes/videoposts/<int:pk>/', views.LikeVideoPost.as_view(), name='like-video-post'),
    #path('likes/videoposts/<int:pk>/detail/', views.LikeVideoPostDetail.as_view(), name='like-video-post-detail'),
]
