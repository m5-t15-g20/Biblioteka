from django.db import models


# Create your models here.
class Copy(models.Model):
    is_available = models.BooleanField(default=True)
    library_name = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name='copy', null=False)
