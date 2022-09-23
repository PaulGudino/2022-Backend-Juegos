from AppJuegos.models import User, Rol, Permission, RolPermission
from AppJuegos.api.serializers import (
    UserSerializer, 
    RolSerializer, 
    PermissionSerializer, 
    RolPermissionSerializer, 
    UserUpdateSerializer,
    CustomRolPermissionSerializer)

from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from rest_framework.response import Response
from rest_framework import status

from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics


class UserCreateViewSet(CRUDViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


class UserViewSet(CRUDViewSet):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes modificar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, pk)

    def destroy(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes eliminar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, pk)
            
class RolViewSet(CRUDViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

    def update(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes modificar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            estado = request.data.get('is_active', None)
            if estado == None or estado == "false":
                user = User.objects.filter(rol=pk)
                if user.exists():
                    for u in user:
                        print(u)
                        u.is_active = False
                        u.save()
            else:
                user = User.objects.filter(rol=pk)
                if user.exists():
                    for u in user:
                        print(u)
                        u.is_active = True
                        u.save()
            return super().update(request, pk)

    def destroy(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes eliminar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

class PermissionViewSet(OnlyListViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

class RolPermissionViewSet(CRUDViewSet):
    serializer_class = RolPermissionSerializer
    queryset = RolPermission.objects.all()




class RolPermissionFilter(generics.ListAPIView):
    serializer_class = CustomRolPermissionSerializer
    queryset = RolPermission.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['rol']
    filterset_fields = ['rol', 'permission']

class RolFilter(generics.ListAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['name']
    filterset_fields = ['name']

class UserFilter(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['rol__name']
    filterset_fields = ['rol']
















