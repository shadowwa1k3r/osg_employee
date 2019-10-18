from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

from app.api.employee.serializers import EmployeeSerializer
from app.model import Group, Employee, Attendance
from rest_framework import serializers


class StaticSerializer(ModelSerializer):
    employee_id = EmployeeSerializer(read_only=True)
    employee_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Attendance
        fields = ('employee_id',
                  'employee_id_id',
                  'date_start',
                  'date_finish')



