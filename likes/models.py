from django.db import models
from django.contrib.auth.models import User
from posts.models import Post, VideoPost


class Like(models.Model):
    """
    Like model, related to 'owner' and'post'.
    'owner' is a User instance.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, related_name='likes', on_delete=models.CASCADE,
        null=True, blank=True
    )

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']

    def __str__(self):
        return f'{self.owner} {self.post}'


class VideoPostLike(models.Model):
    """
    Like model, related to 'owner' and 'video_post'.
    'owner' is a User instance and 'video_post' is a VideoPost instance.
    'unique_together' ensures a user can't like the same post twice.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    video_post = models.ForeignKey(
        VideoPost, related_name='likes', on_delete=models.CASCADE,
        null=True, blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'video_post']

    def __str__(self):
        return f'{self.owner} {self.video_post}'
