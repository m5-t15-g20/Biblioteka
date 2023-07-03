from django.db import models


class Lending(models.Model):
    is_avaliable = models.BooleanField(default=True)
    expire_date = models.DateField()
    lending_date = models.DateField()
    # copy = models.ForeignKey(
    # 	"copies.Copy",
    # 	on_delete=models.CASCADE,
    # 	related_name="leadings",
    # )
    user = models.ForeignKey(
        "users.User",
        on_delete=models.CASCADE,
        related_name="leadings",
    )
