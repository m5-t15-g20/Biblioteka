from rest_framework import serializers, exceptions
from .models import Lending
from datetime import date, timedelta
from django.shortcuts import get_object_or_404
from users.models import User
from rest_framework.response import Response
from rest_framework.views import status
import ipdb


class LeadingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Lending
        fields = ["id", "is_avaliable", "expire_date", "lending_date", "user", "copy"]

    lending_date = serializers.DateField(default=date.today)
    expire_date = serializers.SerializerMethodField()

    def get_expire_date(self, obj):
        today = date.today()
        delta = timedelta(days=7)
        expire_date = today + delta

        if expire_date.weekday() == 5:
            days_to_add = 7 + expire_date.weekday() + 2
            expire_date += timedelta(days=days_to_add)
        if expire_date.weekday() == 6:
            days_to_add = 7 + expire_date.weekday() + 1
            expire_date += timedelta(days=days_to_add)

        return expire_date

    def create(self, validated_data: dict) -> Lending:
        id = self.data["user"]
        user = get_object_or_404(User, pk=id)
        # ipdb.set_trace()
        if user.is_authorized is False:
            raise exceptions.AuthenticationFailed("User not authorized to make a lending")
        return Lending.objects.create(**validated_data)
