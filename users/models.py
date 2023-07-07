from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    user_choices = (
        ("Student", "Student"),
        ("Library Collaborator", "Library Collaborator"),
    )

    email = models.EmailField(
        unique=True, error_messages={"unique": "This field must be unique."}
    )
    is_authorized = models.BooleanField(default=True)
    user_type = models.CharField(
        max_length=20, choices=user_choices, default="Student", blank=True, null=True
    )
    following = models.ManyToManyField("books.Book", related_name="followers")



