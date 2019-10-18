from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView

from app.api.websocket.user.serializers import UserSerializer, UserListSerializer


class UserCreateAPIView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserListAPIView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer


class UserInfoView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    def get_queryset(self):
        queryset = User.objects.filter(username=self.request.user.username)
        print('QUERYSET', queryset)

        return queryset