from django.urls import path, include

# from app.api.employee import views
from app.api.accountant import views

urlpatterns = [
    path('create/', views.Accountant_createAPIView.as_view(), name='api-accountant-create'),
    path('update/<int:id>', views.Accountant_updateAPIView.as_view(), name='api-accountant-update'),
    path('delete/<int:id>', views.Accountant_deleteAPIView.as_view(), name='api-accountant-delete'),
    path('list/', views.Accountant_listAPIView.as_view(), name='api-accountant-list'),
    #

]