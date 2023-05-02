from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAdminUser


from apps.category.models import Category
from apps.category.serializers import CategorySerializer


class CategoryApiViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUser]
