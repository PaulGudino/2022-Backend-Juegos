from AppJuegos.models import (
    GameDate,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.GameDate.GameDateSerializers import (
    GameDateSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class GameDateViewSet(CRUDViewSet):
    serializer_class = GameDateSerializer
    queryset = GameDate.objects.all()



