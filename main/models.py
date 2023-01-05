from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

class Task(models.Model):
    title = models.CharField(max_length=100)
    text = models.CharField(max_length=300, blank=True)
    status = models.BooleanField(default=False)
    date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title
