from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.LikePost.as_view()),
    path('likes/<int:pk>/', views.LikePostDetail.as_view()),
    path('likes/videopost/', views.LikeVideoPost.as_view()),
    path('likes/videopost/<int:pk>', views.LikeVideoPostDetail.as_view())
    #path('videopost-likes/', views.VideoPostLikeList.as_view()), 
    #path('videopost-likes/<int:pk>/', views.VideoPostLikeDetail.as_view()),
]