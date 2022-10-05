from AppJuegos.api.general_api import OnlyListViewSet
from AppJuegos.models import Permission
from AppJuegos.api.Permission.PermissionSerializers import  (
    PermissionSerializer
)




class PermissionViewSet(OnlyListViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()


