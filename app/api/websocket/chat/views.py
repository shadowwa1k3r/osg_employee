from rest_framework.generics import CreateAPIView
from rest_framework.permissions import BasePermission

from app.api.websocket.chat.serializers import ChatSerializer
from app.model import Chat


class IsUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user)


class ChatCreateAPIView(CreateAPIView):
    queryset = Chat.objects.all()
    serializer_class = ChatSerializer
    permission_classes = [IsUser]