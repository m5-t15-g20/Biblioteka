from rest_framework import serializers
from .models import Lending
from datetime import date, timedelta
from users.models import User


class LeadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lending
        fields = ["id", "is_avaliable", "expire_date", "lending_date"]

    lending_date = serializers.DateField(default=date.today)
    expire_date = serializers.SerializerMethodField()

    def get_expire_date(self, obj):
        today = date.today()
        delta = timedelta(days=7)
        expire_date = today + delta

        if expire_date.weekday() >= 5:
            days_to_add = 7 - expire_date.weekday() + 1
            expire_date += timedelta(days=days_to_add)
        return expire_date

    def create(self, validated_data: dict) -> Lending:
        user_id = validated_data["user"]
        user = User.objects.get(id=user_id)
        print(user)
        return Lending.objects.create(**validated_data)
