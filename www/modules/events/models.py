from django.db import models
from django.utils import timezone


class MyEvent(models.Model):
    name = models.TextField()
    date = models.DateTimeField(default=timezone.now)
