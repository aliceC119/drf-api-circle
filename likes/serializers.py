from rest_framework import serializers
from likes.models import Like, VideoPostLike


class LikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the Like model
    The create method handles the unique constraint on 'owner' and 'post'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Like
        fields = ['id', 'created_at', 'owner', 'post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })
class VideoPostLikeSerializer(serializers.ModelSerializer):
    """
    Serializer for the VideoPostLike model
    The create method handles the unique constraint on 'owner' and 'videopost'
    """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = VideoPostLike
        fields = ['id', 'created_at', 'owner', 'video_post']

    def create(self, validated_data):
        try:
            return super().create(validated_data)
        except IntegrityError:
            raise serializers.ValidationError({
                'detail': 'possible duplicate'
            })