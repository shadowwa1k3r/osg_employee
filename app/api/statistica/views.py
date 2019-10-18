from datetime import datetime, timedelta

from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView

from app.api.employee.serializers import EmployeeSerializer, Employee_listSerializer
# from app.api.project.serializers import  Group_listSerialzier, TaskSerialzer, Project_listSerializer
from app.api.position.serializers import PositionSerialzer

from app.api.statistica.serializers import StaticSerializer
from app.model import Group, Employee_group, Employee, Task, Project, Attendance


class Static_listAPIView(ListAPIView):
    serializer_class = StaticSerializer
    queryset = Attendance.objects.all()

    def get_queryset(self):
        N=6
        queryset = Attendance.objects.all()
        e = self.request.GET.get('employee_id')
        # em = Employee.objects.filter(id=e)
        queryset = Attendance.objects.filter(employee_id_id=e)
        queryset = queryset.filter(created__week_day__gte=1)
        # attandance = q.filter(date_start__day=)
        date_N_days_ago = datetime.now() - timedelta(days=N)
        # queryset = queryset.filter(date_start__gte=date_N_days_ago)
        queryset = queryset.order_by('created')[:6]
        print('R',queryset)

        print('Q', date_N_days_ago)

        return queryset

