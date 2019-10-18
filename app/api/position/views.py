from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from app.api.position.serializers import PositionSerialzer, Position_listSerializer
from app.model import Position


class Position_createAPIView(CreateAPIView):
    serializer_class = PositionSerialzer
    queryset = Position.objects.all()
    permission_classes = [IsAdminUser]


class Position_listAPIView(ListAPIView):
    serializer_class = Position_listSerializer
    queryset = Position.objects.all()



