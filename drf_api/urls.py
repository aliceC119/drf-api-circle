"""drf_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import root_route, logout_route
from posts.views import PostList, PostDetail, VideoPostList, VideoPostDetail, SharedPostList, SharedPostDetail, SharedVideoPostList, SharedVideoPostDetail

urlpatterns = [
    path('', root_route),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth/', include('rest_framework.urls')),
    # our logout route has to be above the default one to be matched first
    path('dj-rest-auth/logout/', logout_route),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path(
        'dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')
    ),
    path('api/posts/', PostList.as_view(), name='post-list'), 
    path('api/posts/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('api/videoposts/', VideoPostList.as_view(), name='videopost-list'), 
    path('api/videoposts/<int:pk>/', VideoPostDetail.as_view(), name='videopost-detail'),
    path('api/shared-posts/', SharedPostList.as_view(), name='sharedpost-list'), 
    path('api/shared-posts/<int:pk>/', SharedPostDetail.as_view(), name='sharedpost-detail'),
    path('api/shared-videoposts/', SharedVideoPostList.as_view(), name='sharedvideopost-list'), 
    path('api/shared-videoposts/<int:pk>/', SharedVideoPostDetail.as_view(), name='sharedvideopost-detail'),
    path('', include('profiles.urls')),
    path('', include('posts.urls')),
    path('', include('comments.urls')),
    path('', include('likes.urls')),
    path('', include('followers.urls')),
]
