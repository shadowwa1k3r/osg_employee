from django.db import models


class Task_status(models.Model):
    name = models.CharField(null=True, blank=True, max_length=100)
    created = models.DateField(auto_now_add=True)