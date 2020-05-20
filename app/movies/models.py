from django.db import models
from django.utils import timezone


class Movie(models.Model):
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=255)
    year = models.CharField(max_length=4)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}"
