from django.urls import path

from app.api.statistica import views

urlpatterns = [
    path('list', views.Static_listAPIView.as_view(), name='api-static-list'),
]
