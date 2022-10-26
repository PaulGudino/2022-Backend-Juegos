from AppJuegos.models import (
    AwardGame,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.AwardGame.AwardGameSerializers import (
    AwardGameSerializers
)

from rest_framework import status
from rest_framework.response import Response

class AwardGameViewSet(CRUDViewSet):
    serializer_class = AwardGameSerializers
    queryset = AwardGame.objects.all()

