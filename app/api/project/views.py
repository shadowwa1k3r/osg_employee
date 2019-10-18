from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView


# from app.api.project.serializers import  Group_listSerialzier, TaskSerialzer, Project_listSerializer
from app.api.position.serializers import PositionSerialzer

from app.api.project.serializers import Project_Serialzer, TaskSerialzer, Project_listSerializer, Task_listSerializer
from app.model import Group, Employee_group, Employee, Task, Project


class Project_createAPIView(CreateAPIView):
    serializer_class = Project_Serialzer
    queryset = Project.objects.all()

class Project_updateAPIView(UpdateAPIView):
    serializer_class = Project_Serialzer
    queryset = Project.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)

class Project_deleteAPIView(DestroyAPIView):
    serializer_class = Project_Serialzer
    queryset = Project.objects.all()
    lookup_url_kwarg = 'id'


class Project_listAPIView(ListAPIView):
    serializer_class = Project_listSerializer
    queryset = Project.objects.all()


class Task_createAPIView(CreateAPIView):
    serializer_class = TaskSerialzer
    queryset = Task.objects.all()


class Task_deleteAPIView(DestroyAPIView):
    serializer_class = TaskSerialzer
    queryset = Task.objects.all()
    lookup_url_kwarg = 'id'


class Task_updateAPIView(UpdateAPIView):
    serializer_class = TaskSerialzer
    queryset = Task.objects.all()
    lookup_url_kwarg = 'id'

    def partial_update(self, request, *args, **kwargs):
        kwargs['partial'] = True
        return self.update(request, *args, **kwargs)


class Task_listAPIView(ListAPIView):
    serializer_class = Task_listSerializer
    queryset = Task.objects.all()
#
# class Project_listAPIView(ListAPIView):
#     serializer_class = Project_listSerializer
#     queryset = Project.objects.all()
