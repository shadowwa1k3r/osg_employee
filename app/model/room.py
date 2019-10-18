from django.db import models


class Room(models.Model):
    name = models.TextField(null=True, blank=True)