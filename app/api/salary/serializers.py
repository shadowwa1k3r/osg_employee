from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from app.model import Employee_salary


class Employee_salarySerializer(ModelSerializer):
    # employee_id = Employee_listSerializer(read_only=True)
    employee_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee_salary
        fields = ('employee_id_id',
                  'sum',
                  'date')
