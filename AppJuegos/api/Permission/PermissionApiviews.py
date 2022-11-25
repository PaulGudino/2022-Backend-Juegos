from AppJuegos.api.general_api import OnlyListViewSet
from AppJuegos.models import Permission
from AppJuegos.api.Permission.PermissionSerializers import  (
    PermissionSerializer
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework import generics


class PermissionViewSet(OnlyListViewSet):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()

class PermissionFilter(generics.ListAPIView):
    serializer_class = PermissionSerializer
    queryset = Permission.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter]
    search_fields = ['name']


