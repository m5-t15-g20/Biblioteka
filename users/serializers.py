from rest_framework import serializers
from .models import User
from books.serializers import BookSerializer


class UserSerializer(serializers.ModelSerializer):
    following = BookSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_authorized",
            "is_superuser",
            "type",
            "following",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_authorized": {"read_only": True},
            "is_superuser": {"read_only": True},
            "following": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if (
            "type" in validated_data
            and validated_data["type"] == "Library Collaborator"
        ):
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
