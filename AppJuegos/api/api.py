from AppJuegos.models import User, Rol, Permission, RolPermission
from AppJuegos.api.serializers import UserSerializer, RolSerializer, PermissionSerializer, RolPermissionSerializer

from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet

class UserViewSet(CRUDViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class RolViewSet(CRUDViewSet):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class PermissionViewSet(OnlyListViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

class RolPermissionViewSet(CRUDViewSet):
    serializer_class = RolPermissionSerializer
    queryset = RolPermission.objects.all()













