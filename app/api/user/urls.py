from django.urls import path

from app.api.user import views

urlpatterns = [
    # path('create', views.Position_createAPIView.as_view(), name='api-status-create'),
    path('list', views.Employee_infoListAPIView.as_view(), name='api-user-list')

]