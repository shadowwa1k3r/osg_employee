from django.urls import path, include

from app.api.websocket.room import views

urlpatterns = [
    path('create/', views.RoomCreateAPIView.as_view(), name='api-room-create'),
    path('list/', views.RoomListAPIView.as_view(), name='api-room-list'),

]