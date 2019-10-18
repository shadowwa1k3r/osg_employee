from django.urls import path

from app.api.position import views

urlpatterns = [
    path('create', views.Position_createAPIView.as_view(), name='api-status-create'),
    path('list', views.Position_listAPIView.as_view(), name='api-status-list')

]