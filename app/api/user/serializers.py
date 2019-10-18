from rest_framework.serializers import ModelSerializer, raise_errors_on_nested_writes

from django.contrib.auth.models import User


class UserSerilizer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id',
                  'last_name',
                  'first_name',
                  'username',
                  'email',
                  )


