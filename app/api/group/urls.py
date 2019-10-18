from django.urls import path

from app.api.group import views

urlpatterns = [
    # path('create', views.Position_createAPIView.as_view(), name='api-status-create'),
    path('employee/list', views.Egroup_listAPIView.as_view(), name='api-e-group-list'),
    path('list', views.Group_listAPIView.as_view(), name='api-group-list')

]