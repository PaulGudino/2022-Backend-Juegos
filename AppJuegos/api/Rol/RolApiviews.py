from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from AppJuegos.models import (
    Rol,
    User,
    RolPermission
)
from AppJuegos.api.general_api import CRUDViewSet
from rest_framework import generics
from AppJuegos.api.Rol.RolSerializers import  (
    RolSerializer,
    RolPermissionSerializer,
    CustomRolPermissionSerializer
)

class RolViewSet(CRUDViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

    def create(self, request):
        if (request.data.get('rol_request') != '1'):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        else:
            return super().create(request)
            
    def update(self, request, pk):
        if (request.data.get('rol_request') != '1'):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
        user_rol = User.objects.filter(rol=pk)
        if user_rol.exists():
            rol = self.get_object()
            rol.is_active = False
            rol.save()
            for u in user_rol:
                u.is_active = False
                u.save()
            return Response({'error': 'No puedes eliminar el rol porque tiene usuarios asociados, el rol se desactivará'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

class RolPermissionViewSet(CRUDViewSet):
    serializer_class = RolPermissionSerializer
    queryset = RolPermission.objects.all()

class RolPermissionFilter(generics.ListAPIView):
    serializer_class = CustomRolPermissionSerializer
    queryset = RolPermission.objects.all()
    filter_backends = [SearchFilter, OrderingFilter, DjangoFilterBackend]
    search_fields = ['rol__id', 'permission__name']
    ordering_fields = ['rol', 'permission']
    filterset_fields = ['rol', 'permission']

class RolFilter(generics.ListAPIView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name']
    filterset_fields = ['is_active', 'name']
    ordering_fields = ['created', 'updated']

