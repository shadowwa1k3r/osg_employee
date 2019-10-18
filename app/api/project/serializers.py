from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User


# from app.api.group.serializers import GroupSerializer
from app.api.employee.serializers import Employee_listSerializer
from app.api.group.serializers import GroupSerializer
from app.model import Project, Task
from rest_framework import serializers

from datetime import datetime


class Project_Serialzer(ModelSerializer):
    group_id = GroupSerializer(read_only=True)
    group_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Project
        fields = ('title',
                  'description',
                  'deadline',
                  'group_id',
                  'group_id_id')

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)
        request = self.context['request']
        u = User.objects.get(id=request.user.id)
        if u.employee.position.degree == 9:
            instance.done = True
            instance.done_date = datetime.now()
            instance.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        instance.save()
        return instance


class TaskSerialzer(ModelSerializer):
    class Meta:
        model = Task
        fields = ('task',)

    def create(self, validated_data):
        task = Task(**validated_data)
        task.save()
        p = self.context['request'].data.get('project_id')
        project = Project.objects.get(id=p)
        task.project_id = project
        employee_id = self.context['request'].data.get('employee_id')
        if employee_id:
            task.employee_id_id = employee_id
            task.save()

        return task

    def update(self, instance, validated_data):
        employee = self.context['request'].data.get('employee_id')
        print('eeee', instance.employee_id_id)
        request = self.context['request']
        u = User.objects.get(id=request.user.id)
        if u.employee.id == instance.employee_id_id:

            instance.status_id = request.GET.get('status_id')
        if instance.project_id.group_id.creater == u.employee.id:
            if u.employee.position.degree == 9:
                instance.done = True
                instance.done_date = datetime.now()

        if employee:
            instance.employee_id_id = employee

        instance.save()
        return instance


class Project_listSerializer(ModelSerializer):
    group_id = GroupSerializer(read_only=True)

    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'deadline',
                  'group_id',
                  'created')


class Task_listSerializer(ModelSerializer):
    employee_id = Employee_listSerializer(read_only=True)
    project_id = Project_listSerializer(read_only=True)

    class Meta:
        model = Task
        fields = ('id',
                  'task',
                  'employee_id',
                  'project_id',
                  'created')


