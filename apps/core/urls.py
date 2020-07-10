from rest_framework import routers

from apps.core.views import UserViewSet, GroupViewSet, PermissionViewSet, LogEntryViewSet

# core_router = routers.DefaultRouter()
# core_router.register(r'users', UserViewSet, basename='authentication')
# core_router.register(r'groups', GroupViewSet, basename='group')
# core_router.register(r'permissions', PermissionViewSet, basename='permission')
# core_router.register(r'logs', LogEntryViewSet, basename='log-entry')
