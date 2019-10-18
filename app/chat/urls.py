from django.urls import re_path

# from . import
from app.chat import views

websocket_urlpatterns = [
    re_path(r'ws/chat/(?P<room_name>\w+)/$', views.ChatConsumer),
]