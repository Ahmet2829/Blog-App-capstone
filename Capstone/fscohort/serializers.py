from rest_framework import serializers
from .models import (
    Post,
    PostView,
    Like,
    Comment
)


class PostSerializer(serializers.ModelSerializer):
    comments = serializers.StringRelatedField()
 

    class Meta:
        model = Post
        fields = (
            'title',
            'content',
            'image',
            'publish_date',
            'author',
            'like_count',
            'comment_count',
            'view_count',
            'comments',
            'id'       
        )


class PostViewSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()

    class Meta:
        model = PostView
        fields = ('__all__')


class LikeSerializer(serializers.ModelSerializer):
    created_by = serializers.StringRelatedField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()

    class Meta:
        model = Like
        fields = ('__all__')


class CommentSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    # user_id = serializers.IntegerField()
    post = serializers.StringRelatedField()
    post_id = serializers.IntegerField()

    class Meta:
        model = Comment
        fields = ('__all__')
        # fields = (
        #     'time_stamp',
        #     'content'
        # )
