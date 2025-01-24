from django.urls import path
from comments import views

urlpatterns = [
    path('comments/posts/', views.CommentList.as_view()),
    path('comments/posts/<int:pk>/', views.CommentDetail.as_view()),
#    path('comments/videoposts/', views.CommentList.as_view()),
#    path('comments/videoposts/<int:pk>/', views.CommentDetail.as_view())
]