from django.contrib.auth import authenticate
from django.db import transaction
from rest_framework import status
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from django.shortcuts import get_object_or_404

from apps.users.models import CustomUser
from apps.users.api.serializers import (
    CustomUserSerializer,
    CustomUserListSerializer,
)

class UserViewSet(viewsets.GenericViewSet):
    model = CustomUser
    serializer_class = CustomUserSerializer
    list_serializer_class = CustomUserListSerializer
    queryset = None
    permission_classes = (AllowAny,)

    def get_object(self, pk):
        return get_object_or_404(self.model, pk=pk)

    def get_queryset(self):
        if self.queryset is None:
            self.queryset = self.model.objects.filter(is_active=True).values(
                'id', 'email', 'name', 'last_name', 'password', 'is_staff', 'is_active'
            )
        return self.queryset

    def list(self, request):
        users = self.get_queryset()
        users_serializer = self.list_serializer_class(users, many=True)
        return Response(users_serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        user_serializer = self.serializer_class(data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario registrado correctamente.'
            }, status=status.HTTP_201_CREATED)
        return Response({
            'message': 'Hay errores en el registro',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user)
        return Response(user_serializer.data)
    
    def update(self, request, pk=None):
        user = self.get_object(pk)
        user_serializer = self.serializer_class(user, data=request.data)
        if user_serializer.is_valid():
            user_serializer.save()
            return Response({
                'message': 'Usuario actualizado correctamente'
            }, status=status.HTTP_200_OK)
        return Response({
            'message': 'Hay errores en la actualización',
            'errors': user_serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        try:
            with transaction.atomic():
                user = self.get_object(pk)
                user.is_active = False
                user.save()
            return Response({'message': 'Usuario eliminado correctamente'})
        except self.model.DoesNotExist:
            return Response({'message': 'No existe el usuario que desea eliminar'}, status=status.HTTP_404_NOT_FOUND)

