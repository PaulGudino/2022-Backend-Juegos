from AppJuegos.models import (
    Probabilidad,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Probabilidad.ProbabilidadSerializers import (
    ProbabilidadSerializers,
)

from rest_framework import status
from rest_framework.response import Response

class ProbabilidadViewSet(CRUDViewSet):
    serializer_class = ProbabilidadSerializers
    queryset = Probabilidad.objects.all()

