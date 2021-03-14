from rest_framework import status, viewsets
from rest_framework.response import Response

from posts.serializers.posts import PostSerializer
from posts.services import posts as post_services


class PostViewSet(viewsets.ViewSet):
    def retrieve(self, request, pk=None):
        post = post_services.get_post_by_id(id=pk)

        post_serializer = PostSerializer(data=post.__dict__)
        post_serializer.is_valid(raise_exception=True)

        return Response(post_serializer.data, status=status.HTTP_200_OK)
