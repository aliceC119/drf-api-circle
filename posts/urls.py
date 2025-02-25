from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view(), name='post-detail'),
    path('video-posts/', views.VideoPostList.as_view()),
    path('video-posts/<int:pk>/', views.VideoPostDetail.as_view(),
         name='video-post-detail'),


]
