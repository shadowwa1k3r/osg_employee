from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

from app.api.employee.serializers import Employee_listSerializer
from app.model import Attendance
from rest_framework import serializers


class AttandanceSerialzier(ModelSerializer):
    # employee_id = Employee_listSerializer(read_only=True)
    # employee_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Attendance
        fields = ()




    # def update(self, instance, validated_data):
    #     if instance.
