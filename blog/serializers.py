from rest_framework import serializers
from .models import Comments,Post
from taggit.serializers import (TagListSerializerField,TaggitSerializer)

class PostSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField()

    class Meta:
        model = Post
        fields = '__all__'
        
        
class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'comment', 'created_at', 'post']  # Adjust fields as necessary

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True, source='comment_post')  # Adjust 'source' as needed based on your model's related_name

    class Meta:
        model = Post
        fields = ['id', 'title', 'content', 'publish_date', 'author', 'draft', 'image', 'comments']