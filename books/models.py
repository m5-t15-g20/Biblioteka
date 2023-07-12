from django.db import models
from django.core.validators import MinValueValidator


class Book(models.Model):
    title = models.CharField(max_length=255, null=False, unique=True)
    author = models.CharField(max_length=50, null=False)
    sinopse = models.TextField(null=True, default=None)
    coverImage = models.CharField(max_length=50, null=True, default=None)
    pageQuantity = models.IntegerField(null=False,validators=[MinValueValidator(0)])
