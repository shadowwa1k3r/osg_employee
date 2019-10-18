from django.urls import path, include

urlpatterns = [
    path('chat/', include('app.api.websocket.chat.urls')),
    path('message/', include('app.api.websocket.message.urls')),
    path('room/', include('app.api.websocket.room.urls')),
    path('user/', include('app.api.websocket.user.urls')),

]