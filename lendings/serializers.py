from rest_framework import serializers, exceptions
from .models import Lending
from datetime import date, timedelta


class LeadingSerializer(serializers.ModelSerializer):
    # id = serializers.IntegerField(read_only=True)
    # is_avaliable = serializers.BooleanField(default=True)
    lending_date = serializers.DateField(default=date.today)
    expire_date = serializers.SerializerMethodField()

    class Meta:
        model = Lending
        fields = ["id", "is_avaliable", "expire_date", "lending_date", "user", "copy"]
        # fields = "__all__"
        read_only_fields = ["id"]

    def get_expire_date(self, obj):
        try:
            return self.initial_data["expire_date"]
        except Exception:
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
        # ipdb.set_trace()
        user = validated_data["user"]

        if user.is_authorized is False:
            raise exceptions.AuthenticationFailed(
                "User not authorized to make a lending"
            )
        # ipdb.set_trace()

        return Lending.objects.create(**validated_data)
