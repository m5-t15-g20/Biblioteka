from rest_framework import serializers
from .models import User

from django.contrib.auth.hashers import make_password


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "password",
            "is_authorized",
            "is_superuser",
            "user_type",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_authorized": {"read_only": True},
            "is_superuser": {"read_only": True},
        }

    def create(self, validated_data: dict) -> User:
        if (
            "user_type" in validated_data
            and validated_data["user_type"] == "Library Collaborator"
        ):
            return User.objects.create_superuser(**validated_data)

        return User.objects.create_user(**validated_data)
