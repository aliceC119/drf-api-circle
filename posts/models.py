from django.db import models
from django.contrib.auth.models import User
from .validators import validate_youtube_url

TYPE_CHOICES = [
    ('text', 'Text'),
    ('image', 'Image'),
    ('video', 'Video'),
    ('tutorial', 'Tutorial'),
    ('youtube', 'YouTube')
]


class Post(models.Model):
    """
    Post model, related to 'owner', i.e. a User instance.
    Default image set so that we can always reference image.url.
    """
    image_filter_choices = [
        ('_1977', '1977'), ('brannan', 'Brannan'),
        ('earlybird', 'Earlybird'), ('hudson', 'Hudson'),
        ('inkwell', 'Inkwell'), ('lofi', 'Lo-Fi'),
        ('kelvin', 'Kelvin'), ('normal', 'Normal'),
        ('nashville', 'Nashville'), ('rise', 'Rise'),
        ('toaster', 'Toaster'), ('valencia', 'Valencia'),
        ('walden', 'Walden'), ('xpro2', 'X-pro II')
    ]

    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    image = models.ImageField(
        upload_to='images/', default='../default_post_mgvuq6', blank=True
    )
    image_filter = models.CharField(
        max_length=32, choices=image_filter_choices, default='normal'
    )
    type = models.CharField(
        max_length=32, choices=TYPE_CHOICES, default='text'
    )

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('post-detail')

    def __str__(self):
        return f'{self.id} {self.title}'


class VideoPost(models.Model):
    video_filter_choices = [
        ('normal', 'Normal'),
        ('sepia', 'Sepia'),
        ('grayscale', 'Grayscale')
    ]

    name = models.CharField(max_length=100, blank=True, null=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    video_filter = models.CharField(
        max_length=32, choices=video_filter_choices, default='normal'
    )
    youtube_url = models.URLField(
        validators=[validate_youtube_url], blank=True, null=True
    )
    comments = models.TextField(blank=True)
    type = models.CharField(
        max_length=32, choices=TYPE_CHOICES, default='video'
    )

    class Meta:
        ordering = ['-created_at']

    def get_absolute_url(self):
        return reverse('video-detail')

    def __str__(self):
        return f'{self.id} {self.title}'
