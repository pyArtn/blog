from rest_framework.viewsets import ModelViewSet

from apps.user.models import User
from apps.user.serializers import UserSerializer, UserCreateSerializer


class UserApiViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_serializer_class(self):
        if self.action == "create":
            return UserCreateSerializer
        return UserSerializer
