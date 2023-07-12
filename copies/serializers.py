from .models import Copy
from rest_framework import serializers


class CopySerializers(serializers.ModelSerializer):
    class Meta:
        depth = 1
        model = Copy
        fields = ["id", "is_available", "library_name", "created_at", "book"]
        extra_kwargs = {
            "id": {"read_only": True},
        }

    def create(self, validated_data: dict) -> Copy:
        return Copy.objects.create(**validated_data)