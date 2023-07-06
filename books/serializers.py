from rest_framework import serializers
from .models import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "sinopse", "coverImage", "pageQuantity"]

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)
