from rest_framework import serializers
from post.models import Post,Vote

class PostSerializer(serializers.ModelSerializer):
    
    poster=serializers.ReadOnlyField(source='poster.poster')
    poster_id=serializers.ReadOnlyField(source='poster.id')
    class Meta:
        model=Post
        fields=['id','title','url','poster','poster_id','created']
        
class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model=Vote
        fields=['id','voter','post']

