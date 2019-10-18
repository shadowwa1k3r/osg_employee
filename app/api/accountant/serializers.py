from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

from app.api.employee.serializers import Employee_listSerializer
from app.model import Accountant
from rest_framework import serializers


class AccountantSerializer(ModelSerializer):
    employee = Employee_listSerializer(read_only=True)
    employee_id = serializers.IntegerField(write_only=True)
    accounter = Employee_listSerializer(read_only=True)
    accounter_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Accountant
        fields = ('employee',
                  'employee_id',
                  'sum',
                  'date',
                  'accounter',
                  'accounter_id',
                  )

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            # setattr(instance.employee_group, attr, value)

        instance.save()
        # instance.employee_group.save()

        return instance


class Accountant_listSerialzier(ModelSerializer):
    employee = Employee_listSerializer(read_only=True)
    accounter = Employee_listSerializer(read_only=True)

    class Meta:
        model = Accountant
        fields = ('id',
                  'employee',
                  'date',
                  'sum',
                  'accounter')

