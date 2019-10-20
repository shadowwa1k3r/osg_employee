from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

# from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer, Employee_groupSerializer
from rest_framework.permissions import IsAuthenticated, IsAdminUser, BasePermission

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer, Employee_groupSerializer, Group_listSerialzier
from app.api.position.serializers import PositionSerialzer
from app.api.salary.serializers import Employee_salarySerializer
from app.model import Position, Employee, Group, Employee_group
from app.model.user import Employee_salary


class IsManagerUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.employee.position.degree == 9)


class Employee_createAPIView(CreateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser]

    # def get_queryset(self):
    #     qs = Employee.objects.all()
    #     u = User.objects.all(username=self.request.user.username)
    #     if u.is_superuser:

class Employee_updateAPIView(UpdateAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsAdminUser]

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class Employee_deleteAPIView(DestroyAPIView):
    serializer_class = EmployeeSerializer
    queryset = Employee.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsAdminUser]


class Employee_listAPIView(ListAPIView):
    serializer_class = Employee_listSerializer
    queryset = Employee.objects.all()
    permission_classes = [IsAdminUser, IsManagerUser]

    def get_queryset(self):
        qs = Employee.objects.all()
        id = self.request.GET.get('id')
        if id:
            qs = qs.filter(id=id)
        return qs



class Employee_groupCreateapiView(CreateAPIView):
    serializer_class = Employee_groupSerializer
    queryset = Employee_group.objects.all()
    permission_classes = [IsManagerUser]



class Employee_groupUpdateView(UpdateAPIView):
    serializer_class = Employee_groupSerializer
    queryset = Employee_group.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsManagerUser]


class Employee_grouplistAPIView(ListAPIView):
    serializer_class = Group_listSerialzier
    queryset = Employee_group.objects.all()

class Employee_groupdeleteAPIView(DestroyAPIView):
    serializer_class = Employee_groupSerializer
    queryset = Employee_group.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsManagerUser]


class IsAccountantUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.employee.position.degree == 7)


class Employee_salaryCreateAPIView(CreateAPIView):
    serializer_class = Employee_salarySerializer
    queryset = Employee_salary.objects.all()
    permission_classes = [IsAccountantUser]







# class Group_createAPIView(CreateAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#
# class Group_updateAPIView(UpdateAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#     lookup_url_kwarg = 'id'
#
#     def partial_update(self, request, *args, **kwargs):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
#
# class Group_deleteAPIView(DestroyAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()
#     lookup_url_kwarg = 'id'
#
# class Group_listAPIView(ListAPIView):
#     serializer_class = Group_Serialzier
#     queryset = Group.objects.all()

    # def get_queryset(self):
    #     id = self.request.data.get('id')
    #     u = Employee.objects.get(employee_id_id=id)
    #     if self.request.user.is_staff:
    #         if u == 'director':
    #             print()



