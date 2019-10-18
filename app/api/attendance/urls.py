from django.urls import path, include

# from app.api.employee import views
from app.api.attendance import views

urlpatterns = [
    path('create/', views.Attandance_createAPIView.as_view(), name='api-attendance-create'),
    # path('update/<int:id>', views.Employee_updateAPIView.as_view(), name='api-employee-update'),
    # path('delete/<int:id>', views.Employee_deleteAPIView.as_view(), name='api-employee-delete'),
    # path('list/', views.Employee_listAPIView.as_view(), name='api-employee-list'),
    #

]