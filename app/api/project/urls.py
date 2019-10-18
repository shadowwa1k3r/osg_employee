from django.urls import path

from app.api.project import views

urlpatterns = [
    path('create', views.Project_createAPIView.as_view(), name='api-project-create'),
    path('update/<int:id>', views.Project_updateAPIView.as_view(), name='api-project-update'),
    path('delete/<int:id>', views.Project_deleteAPIView.as_view(), name='api-project-delete'),
    path('list', views.Project_listAPIView.as_view(), name='api-project-list'),

    path('task/create', views.Task_createAPIView.as_view(), name='api-project-task-create'),
    path('task/update/<int:id>', views.Task_updateAPIView.as_view(), name='api-project-task-update'),
    path('task/delete/<int:id>', views.Task_deleteAPIView.as_view(), name='api-project-task-delete'),
    path('task/list', views.Task_listAPIView.as_view(), name='api-project-list')
]