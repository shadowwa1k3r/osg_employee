from django.urls import path, include

from app.api.websocket.message import views

urlpatterns = [
    path('create/', views.MessageCreateAPIView.as_view(), name='api-message-create'),
    # path('list/', views.UserListAPIView.as_view(), name='api-user-list'),
    # path('info/', views.UserInfoView.as_view(), name='api-user-info'),

]