from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from app.api.employee.serializers import EmployeeGroupSerializer
from app.api.group.serializers import GroupSerializer
from app.api.position.serializers import PositionSerialzer

from app.model import Employee, Employee_group, Group


class Egroup_listAPIView(ListAPIView):
    serializer_class = EmployeeGroupSerializer
    queryset = Employee_group.objects.all()


class Group_listAPIView(ListAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer