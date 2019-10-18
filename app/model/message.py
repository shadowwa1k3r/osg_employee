from django.contrib.auth.models import User
from django.db import models

from app.model.room import Room


class Message(models.Model):
    room_id = models.ForeignKey(Room, on_delete=models.SET_NULL, null=True)
    sender_id = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    message = models.TextField(null=True, blank=True)