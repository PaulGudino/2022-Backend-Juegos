from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from AppJuegos.models import (
    Rol,
    User,
    RolPermission
)
from AppJuegos.api.general_api import CRUDViewSet
from rest_framework import generics
from rest_framework.decorators import action 
from AppJuegos.api.Rol.RolSerializers import  (
    RolSerializer,
    RolPermissionSerializer,
    CustomRolPermissionSerializer
)

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
                        u.is_active = False
                        u.save()
            else:
                user = User.objects.filter(rol=pk)
                if user.exists():
                    for u in user:
                        u.is_active = True
                        u.save()
            return super().update(request, pk)

    def destroy(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes eliminar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

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



