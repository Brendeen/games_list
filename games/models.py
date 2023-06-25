from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse


class Game(models.Model):
    name = models.CharField(max_length=256)
    year = models.DateField(null=True, default=0)
    description = models.TextField(null=True, default="Video Game")

    def __str__(self):
        return self.name
