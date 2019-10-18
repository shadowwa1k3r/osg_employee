from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

# from app.api.employee.serializers import EmployeeSerializer

from app.model import Group, Project, Task
from rest_framework import serializers


class TaskForProjectListSerializer(ModelSerializer):

    class Meta:
        model = Task
        fields = ('id',
                  'task',
                  'done',
                  'done_date')


class ProjectForGroupListSerializer(ModelSerializer):
    task_set = TaskForProjectListSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('id',
                  'title',
                  'description',
                  'deadline',
                  'task_set',
                  )


class GroupSerializer(ModelSerializer):
    # creater = serializers.IntegerField(read_only=True)
    project_set = ProjectForGroupListSerializer(many=True, read_only=True)

    class Meta:
        model = Group
        fields = ('id',
                  'name',
                  'creater',
                  'project_set')

