from rest_framework.serializers import ModelSerializer

from app.api.websocket.room.serializers import RoomSerializer
from app.api.websocket.user.serializers import UserSerializer
from app.model import Chat
from rest_framework import serializers


class ChatSerializer(ModelSerializer):
    room_id = RoomSerializer(read_only=True)
    room_id_id = serializers.IntegerField(write_only=True)
    user_id = UserSerializer(read_only=True)
    user_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Chat
        fields = ('room_id',
                  'room_id_id',
                  'user_id',
                  'user_id_id')
