import django.contrib.auth.password_validation as pwd_validator
from django.contrib.auth.models import User
from django.core import exceptions
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8, max_length=200, write_only=True)

    class Meta:
        model = User
        fields = [
            'url', 'username', 'email', 'is_staff', 'is_superuser', 'last_login', 'date_joined',
            'first_name', 'last_name', 'password',
        ]
        read_only_fields = ['date_joined', 'last_login']

    # def update(self, instance, validated_data):
    #     password = validated_data.pop('password', None)
    #     for (key, value) in validated_data.items():
    #         setattr(instance, key, value)
    #
    #     if password is not None:
    #         instance.set_password(password)
    #
    #     instance.save()
    #     return instance

    # def delete(self, instance, *args, **kwargs):
    #     instance.is_active = False
    #     instance.save()
    #     return instance
    #
    # def undelete(self, instance, *args, **kwargs):
    #     instance.is_active = True
    #     instance.save()
    #     return instance
