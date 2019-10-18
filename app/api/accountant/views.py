from rest_framework.generics import CreateAPIView, UpdateAPIView, DestroyAPIView, ListAPIView
from rest_framework.permissions import BasePermission
from rest_framework.response import Response
from rest_framework.views import APIView

from app.api.accountant.serializers import AccountantSerializer, Accountant_listSerialzier
from app.api.attendance.serializers import AttandanceSerialzier
from app.model import Accountant
from datetime import datetime


class IsAccountantUser(BasePermission):

    def has_permission(self, request, view):
        return bool(request.user and request.user.employee.position.degree == 7)


class Accountant_createAPIView(CreateAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()
    permission_classes = [IsAccountantUser]


class Accountant_updateAPIView(UpdateAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsAccountantUser]


class Accountant_deleteAPIView(DestroyAPIView):
    serializer_class = AccountantSerializer
    queryset = Accountant.objects.all()
    lookup_url_kwarg = 'id'
    permission_classes = [IsAccountantUser]


class Accountant_listAPIView(ListAPIView):
    serializer_class = Accountant_listSerialzier
    queryset = Accountant.objects.all()
    print('l')

    def get_queryset(self):
        qs = Accountant.objects.all()
        if self.request.GET.get('month'):
            qs = qs.filter(date__month=self.request.GET.get('month'))
        if self.request.GET.get('employee_id'):
            qs = qs.filter(employee_id=self.request.GET.get('employee_id'))

        return qs



