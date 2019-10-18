from django.contrib.auth.models import User
from rest_framework.serializers import ModelSerializer
from rest_framework import serializers

from app.model import Chat, Message, Room


class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'username',)


class MessageListSerializer(ModelSerializer):
    sender_id = UserSerializer(read_only=True)
    sender_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Message
        fields = ('room_id',
                  'room_id_id',
                  'sender_id',
                  'sender_id_id',
                  'message')


class ChatListSerializer(ModelSerializer):
    user_set = serializers.SerializerMethodField(read_only=True)
    message_set = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Chat
        fields = ('id',
                  'room_id_id',
                  'user_set',
                  'message_set')

    def get_message_set(self, obj):
        qs = Message.objects.filter(room_id__chat=obj)
        message_serializer = MessageListSerializer(qs, many=True)
        return message_serializer.data

    def get_user_set(self, obj):
        room_id = obj.room_id
        qs = User.objects.filter(chat__room_id=room_id)
        user_serializer = UserSerializer(qs, many=True)
        return user_serializer.data


class UserListSerializer(ModelSerializer):
    chat_set = ChatListSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ('id',
                  'username',
                  'password',
                  'chat_set')

