from rest_framework.viewsets import ModelViewSet

from apps.post.models import Post
from apps.post.serializers import PostSerializer


class PostApiViewSet(ModelViewSet):
    queryset = Post.objects.prefetch_related("categories").select_related("owner").all()
    serializer_class = PostSerializer
