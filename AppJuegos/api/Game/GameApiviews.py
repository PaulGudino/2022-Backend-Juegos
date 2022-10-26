from AppJuegos.models import (
    Game,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Game.GameSerializers import (
    GameSerializers,
)

from rest_framework import status
from rest_framework.response import Response

class GameViewSet(CRUDViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()

