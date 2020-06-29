# ViewSets define the view behavior.
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.core.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def list(self, request, **kwargs):
        queryset = self.queryset.filter(is_active=True)
        serializer = self.serializer_class(queryset, context={'request': request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, pk=None, **kwargs):
        queryset = self.queryset.filter(is_active=True)
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserSerializer(user, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, pk=None, **kwargs):
        serializer = self.serializer_class(request.data, context={'request': request})
        password = request.data['password']
        del(request.data['password'])

        if serializer.validate(request.data):
            user = User(**request.data)
            user.set_password(password)
            user.save()
            return Response(self.serializer_class(user, context={'request': request}).data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors)

    def update(self, request, pk=None, **kwargs):
        queryset = self.queryset.filter(is_active=True)
        user = get_object_or_404(queryset, pk=pk)

        if request.data['password']:
            user.set_password(request.data['password'])
            del(request.data['password'])

        serializer = self.serializer_class(user, context={'request': request}, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, pk=None, **kwargs):
        queryset = self.queryset.filter(is_active=True)
        user = get_object_or_404(queryset, pk=pk)
        user.is_active = False
        user.save()

        return Response(status=204)
