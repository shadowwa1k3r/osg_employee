from rest_framework.generics import CreateAPIView, ListAPIView

from app.api.websocket.room.serializers import RoomSerializer
from app.model import Room


class RoomCreateAPIView(CreateAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomListAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer