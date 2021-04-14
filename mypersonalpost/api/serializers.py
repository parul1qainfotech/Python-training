from api.models import Post,Like
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    user=serializers.ReadOnlyField(source='user.user')
    class Meta:
        model=Post
        fields=['id','title','post','created','updated','user']
        
class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Like
        fields=['post_by','liked_by']