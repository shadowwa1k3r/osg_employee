from rest_framework.generics import CreateAPIView

from app.api.websocket.message.serializers import MessageSerializer
from app.model import Message


class MessageCreateAPIView(CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer