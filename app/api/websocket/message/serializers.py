from rest_framework.serializers import ModelSerializer

from app.api.websocket.room.serializers import RoomSerializer
from app.api.websocket.user.serializers import UserSerializer
from app.model import Message
from rest_framework import serializers


class MessageSerializer(ModelSerializer):
    room_id = RoomSerializer(read_only=True)
    room_id_id = serializers.IntegerField(write_only=True)
    sender_id = UserSerializer(read_only=True)
    sender_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = ('room_id',
                  'room_id_id',
                  'sender_id',
                  'sender_id_id',
                  'message')
