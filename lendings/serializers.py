from rest_framework import serializers, exceptions
from .models import Lending
from datetime import date
from users.models import User
import ipdb


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "email",
            "is_authorized",
            "is_superuser",
            "type",
        ]
        read_only_fields = ["password", "id"]


class LeadingSerializer(serializers.ModelSerializer):
    lending_date = serializers.DateField(default=date.today)
    expire_date = serializers.DateField()
    user = UserSerializer(read_only=True)

    class Meta:
        depth = 2
        model = Lending
        fields = "__all__"

    def create(self, validated_data: dict) -> Lending:

        user = validated_data["user"]
        copy = validated_data["copy"]
        if user.is_authorized is False:
            raise exceptions.PermissionDenied(
                "User not authorized to make a lending"
            )
        if copy.is_available is False:
            raise exceptions.PermissionDenied(
                "Copy not available for lending"
            )
        else:
            copy.is_available = False
            copy.save()

        return Lending.objects.create(**validated_data)


class LendginCreate(LeadingSerializer):
    expire_date = serializers.DateField(read_only=True)


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField()
