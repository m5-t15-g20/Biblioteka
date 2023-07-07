from rest_framework import serializers
from .models import Book
from users.models import User


class UserFollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email"]


class BookSerializer(serializers.ModelSerializer):
    followers = UserFollowSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "author",
            "sinopse",
            "coverImage",
            "pageQuantity",
            "followers",
        ]
        extra_kwargs = {
            "followers": {"read_only": True},
        }

    def create(self, validated_data: dict) -> Book:
        book_created = Book.objects.create(**validated_data)
        return book_created


class FollowingSerializer(serializers.ModelSerializer):
    followers = UserFollowSerializer(many=True, read_only=True)

    class Meta:
        model = Book
        fields = ["followers"]
        depth: 1
