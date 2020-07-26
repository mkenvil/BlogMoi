from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=400, null=True)
    author = models.CharField(max_length=200, null=True)
    context = models.TextField(null=True)
    date_created = models.DateTimeField(default=timezone.now)

    class Meta:
        verbose_name_plural = "Post"

    def __str__(self):
        return self.title


