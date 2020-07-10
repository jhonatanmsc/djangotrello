from rest_framework import routers

from apps.authentication.views import UserViewSet, GroupViewSet, PermissionViewSet, LogEntryViewSet

auth_router = routers.DefaultRouter()
auth_router.register(r'users', UserViewSet, basename='user')
auth_router.register(r'groups', GroupViewSet, basename='group')
auth_router.register(r'permissions', PermissionViewSet, basename='permission')
auth_router.register(r'logs', LogEntryViewSet, basename='log-entry')
