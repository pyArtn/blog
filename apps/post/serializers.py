from rest_framework.serializers import ModelSerializer

from apps.post.models import Post
from apps.category.serializers import CategorySerializer
from apps.user.serializers import UserSerializer


class PostSerializer(ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    owner = UserSerializer(read_only=True)

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "description",
            "created_at",
            "owner",
            "categories",
        )
