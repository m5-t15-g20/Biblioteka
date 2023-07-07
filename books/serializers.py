from rest_framework import serializers
from .models import Book, Favorite


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ["id", "title", "author", "sinopse", "coverImage", "pageQuantity"]

    def create(self, validated_data: dict) -> Book:
        return Book.objects.create(**validated_data)


class FavoriteSerializer(serializers.ModelField):
    class Meta:
        model = Favorite
        fields = ["id", "follow", "user", "book"]

    def create(self, validated_data: dict, user, book) -> Favorite:
        print(validated_data)
        return Favorite.objects.create(**validated_data, user=user, book=book)
