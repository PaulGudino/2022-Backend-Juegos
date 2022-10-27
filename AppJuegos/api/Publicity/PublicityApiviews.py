from AppJuegos.models import (
    Publicity,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Publicity.PublicitySerializers import (
    PublicitySerializers,
)

from rest_framework import status
from rest_framework.response import Response

class PublicityViewSet(CRUDViewSet):
    serializer_class = PublicitySerializers
    queryset = Publicity.objects.all()

