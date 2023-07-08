from .models import Copy
from django.views import View
from rest_framework import status, serializers
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from books.models import Book
# from rest_framework.validators import UniqueValidator


class CopySerializers(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = ["id", "is_available", "library_name", "created_at", "book"]
        extra_kwargs = {
            "id": {"read_only": True},
            # "book": {"read_only": True}
        }

    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)