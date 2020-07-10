from django.contrib.admin.models import LogEntry
from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    password = serializers.CharField(min_length=8, max_length=200, write_only=True)

    class Meta:
        model = User
        fields = '__all__'
        read_only_fields = ['date_joined', 'last_login']


class GroupSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Group
        fields = '__all__'


class PermissionSerializer(serializers.HyperlinkedModelSerializer):
    app_label = serializers.CharField(source='content_type.app_label')
    model_name = serializers.CharField(source='content_type.model')

    class Meta:
        model = Permission
        fields = ['name', 'codename', 'app_label', 'model_name']


class LogEntrySerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = LogEntry
        fields = ['action_time', 'object_id', 'object_repr', 'action_flag', 'change_message', 'authentication']
