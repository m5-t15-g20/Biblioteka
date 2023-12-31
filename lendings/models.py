from django.db import models
from datetime import date, timedelta


class Lending(models.Model):
    is_close = models.BooleanField(default=False)
    expire_date = models.DateField(default=date.today() + timedelta(days=7))
    lending_date = models.DateField()
    copy = models.ForeignKey(
        "copies.Copy",
        on_delete=models.CASCADE,
        related_name="leadings",
    )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="leadings",
    )
