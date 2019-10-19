from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes
from django.contrib.auth.models import User

# from app.api.project.serializers import Employee_groupSerializer
from app.api.group.serializers import GroupSerializer


from app.api.salary.serializers import Employee_salarySerializer

from app.api.user.serializers import UserSerilizer
from app.model import Employee, Employee_group, Attendance
from rest_framework import serializers
from app.api.position.serializers import PositionSerialzer


class EmployeeSerializer(ModelSerializer):
    position = PositionSerialzer(read_only=True)
    position_id = serializers.IntegerField(write_only=True)
    username = serializers.CharField(write_only=True)
    first_name = serializers.CharField(write_only=True)
    last_name = serializers.CharField(write_only=True)
    email = serializers.EmailField(write_only=True)
    is_active = serializers.BooleanField(write_only=True)
    password = serializers.CharField(write_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  'username',
                  'first_name',
                  'last_name',
                  'email',
                  'is_active',
                  'password',
                  'position_id',
                  )

    def create(self, validated_data):
        username = validated_data.pop('username')
        #     _id = serializers.IntegerField(write_only=True)
        firstname = validated_data.pop('first_name')
        lastname = validated_data.pop('last_name')
        email = validated_data.pop('email')
        is_active = validated_data.pop('is_active')
        password = validated_data.pop('password')

        employee = Employee(**validated_data)
        u = User.objects.create(username=username, first_name=firstname, last_name=lastname, email=email,
                                is_active=is_active)
        u.set_password(password)
        u.save()
        employee.user = u
        employee.save()
        return employee

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        if validated_data.get('password'):
            p = validated_data.pop('password')
            instance.user.set_password(p)
        for attr, value in validated_data.items():
            setattr(instance.user, attr, value)
            setattr(instance, attr, value)

        instance.user.save()
        instance.save()

        return instance


class Employee_groupSerializer(ModelSerializer):
    employee_group = GroupSerializer(read_only=True)
    employee_id = EmployeeSerializer(read_only=True)
    employee_id_id = serializers.IntegerField(write_only=True)
    employee_group_id = serializers.IntegerField(write_only=True)

    # employee_id = EmployeeSerializer(read_only=True)

    class Meta:
        model = Employee_group
        fields = ('employee_group',
                  'employee_id',
                  'employee_group_id',
                  'employee_id_id',
                  )

    def update(self, instance, validated_data):
        raise_errors_on_nested_writes('update', self, validated_data)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
            # setattr(instance.employee_group, attr, value)

        instance.save()
        # instance.employee_group.save()

        return instance


class AttandanceSerialzier(ModelSerializer):
    # employee_id = Employee_listSerializer(read_only=True)
    # employee_id_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Attendance
        fields = ('id', 'date_start', 'date_finish')


class Employee_listSerializer(ModelSerializer):
    user = UserSerilizer()
    employee_group_set = Employee_groupSerializer(many=True, read_only=True)
    attendance_set = AttandanceSerialzier(many=True, read_only=True)
    status = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'user',
                  'employee_group_set',
                  'attendance_set',
                  'status')

    def get_status(self, obj):
        resp = False
        aset = Attendance.objects.filter(employee_id=obj)
        if aset.count()>0:
            today = aset.last()
            if today.date_start:
                resp = True
            if today.date_finish:
                resp = False
        return resp

    def to_representation(self, instance):
        employee_status = super(Employee_listSerializer, self).to_representation(instance)
        print('111', instance.position.degree)
        if self.context['request'].user.employee.position.degree == 9:
            pass
        elif self.context['request'].user.employee.position.degree == 8:
            employee_status.pop('employee_group_set')

        elif self.context['request'].user.employee.position.degree == 7:
            employee_status.pop('employee_group_set')
        elif self.context['request'].user.employee.position.degree == 6:
            employee_status.pop('image')
            employee_status.pop('phone')
            employee_status.pop('address')
            employee_status.pop('position')
            employee_status.pop('user')
            employee_status.pop('employee_group_set')
            employee_status.pop('employee_attendance_set')


        return employee_status


class   Group_listSerialzier(ModelSerializer):
    employee_id = Employee_listSerializer(read_only=True)
    employee_group = GroupSerializer(read_only=True)

    class Meta:
        model = Employee_group
        fields = ('id',
                  'employee_id',
                  'employee_group')


class EmployeeGroupSerializer(ModelSerializer):
    employee_id = EmployeeSerializer(read_only=True)
    employee_id_id = serializers.IntegerField(write_only=True)
    employee_group = GroupSerializer(read_only=True)
    employee_group_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Employee_group
        fields = ('employee_id_id',
                  'employee_group_id',
                  'employee_id',
                  'employee_group')


class Employee_infoSerializer(ModelSerializer):
    position = PositionSerialzer(read_only=True)
    user = UserSerilizer(read_only=True)
    employee_salary_set = Employee_salarySerializer(read_only=True, many=True)
    employee_group_set = EmployeeGroupSerializer(read_only=True, many=True)

    class Meta:
        model = Employee
        fields = ('id',
                  'user',
                  'image',
                  'phone',
                  'address',
                  'position',
                  'gender',
                  'employee_salary_set',
                  'employee_group_set',
                  )




