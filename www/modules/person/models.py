from django.db import models


class MyUser(models.Model):
    name = models.TextField()
    email = models.TextField()
