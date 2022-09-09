from AppJuegos.models import User, Rol, Permission, RolPermission
from AppJuegos.api.serializers import UserSerializer, RolSerializer, PermissionSerializer, RolPermissionSerializer

from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from rest_framework.response import Response
from rest_framework import status


class UserViewSet(CRUDViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

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
            print('Modificando rol')
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













