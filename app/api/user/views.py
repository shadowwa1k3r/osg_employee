# Employee_infoSerializer
from rest_framework.generics import CreateAPIView, UpdateAPIView, ListAPIView
from rest_framework.permissions import IsAdminUser

from app.api.employee.serializers import Employee_infoSerializer
from app.api.position.serializers import PositionSerialzer

from app.model import Employee


class Employee_infoListAPIView(ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = Employee_infoSerializer

    def get_queryset(self):
        qs = Employee.objects.all()
        if self.request.user:
            qs = qs.filter(user=self.request.user)

        return qs



