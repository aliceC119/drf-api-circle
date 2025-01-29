import re
from django.core.exceptions import ValidationError

# Regular expression to match valid YouTube URLs and extract video ID
YOUTUBE_REGEX = re.compile(
    r'^(https?\:\/\/)?(www\.)?(youtube\.com\/(watch\?v=|embed\/|v\/)|youtu\.be\/)([a-zA-Z0-9_-]{11}).*$'
)

def validate_youtube_url(value):
    """
    Validate that the value is a valid YouTube URL.
    """
    if not isinstance(value, str):
        raise ValidationError("Invalid input type. Expected a string.")

    if not value.strip():
        raise ValidationError("YouTube URL cannot be empty.")

    match = YOUTUBE_REGEX.match(value)
    if not match:
        raise ValidationError("This is not a valid YouTube URL. Please provide a valid link.")

    # Optional: Extract the video ID
    video_id = match.group(5)

    # Return the validated URL instead of just the video ID
    return value
