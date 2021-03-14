from rest_framework import serializers


class PostSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    pub_date = serializers.DateTimeField()


class ReviewSerializer(serializers.Serializer):
    title = serializers.CharField()
    description = serializers.CharField()
    username = serializers.CharField()
