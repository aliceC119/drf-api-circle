from django.urls import path
from comments import views

urlpatterns = [
    path('comments/posts/', views.CommentList.as_view()),
    path('comments/posts/<int:pk>/', views.CommentDetail.as_view()),
    path('comments/video-posts/', views.VideoPostCommentList.as_view()),
    path('comments/video-posts/<int:pk>/', views.VideoPostCommentDetail.as_view())
]