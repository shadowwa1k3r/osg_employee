from django.urls import path, include

from app.api.websocket.user import views

urlpatterns = [
    path('create/', views.UserCreateAPIView.as_view(), name='api-user-create'),
    path('list/', views.UserListAPIView.as_view(), name='api-user-list'),
    path('info/', views.UserInfoView.as_view(), name='api-user-info'),

]