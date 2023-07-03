from django.db import models

# Create your models here.
class Copy(models.Model):
    libraryName = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    book_id = models.ManyToOneRel("", on_delete=models.CASCADE, related_name='', null=False)
