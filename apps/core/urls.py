from rest_framework import routers

from apps.core.api import UserViewSet

core_router = routers.DefaultRouter()
core_router.register(r'users', UserViewSet, basename='user')
