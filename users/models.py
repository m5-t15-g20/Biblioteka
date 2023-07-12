from django.db import models
from django.contrib.auth.models import AbstractUser

class User_choices(models.TextChoices):
    student = "Student"
    library_collaborator = "Library Collaborator"

class User(AbstractUser):
    # user_choices = (
    #     ("Student", "Student"),
    #     ("Library Collaborator", "Library Collaborator"),
    # )

    email = models.EmailField(
        unique=True, error_messages={"unique": "This field must be unique."}
    )
    is_authorized = models.BooleanField(default=True)
    type = models.CharField(
        max_length=20, choices=User_choices.choices, default=User_choices.student, blank=True, null=True
    )
    following = models.ManyToManyField("books.Book", related_name="followers")
