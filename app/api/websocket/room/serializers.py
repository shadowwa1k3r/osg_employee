from rest_framework.serializers import ModelSerializer

from app.model.room import Room


class RoomSerializer(ModelSerializer):
    class Meta:
        model = Room
        fields = ('name',
                  )