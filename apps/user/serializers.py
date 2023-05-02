from rest_framework.serializers import ModelSerializer

from apps.user.models import User


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "image",
            "bio",
        )


class UserCreateSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "image",
            "bio",
            "password",
        )

    def create(self, validated_data):
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.is_active = True
        user.save()
        return user
