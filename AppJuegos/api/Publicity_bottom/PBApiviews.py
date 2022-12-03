import os
from AppJuegos.models import (
    Publicity_bottom,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Publicity_bottom.PBSerializers import (
    PBSerializer,
)
from rest_framework import status
from rest_framework.response import Response

class PBViewSet(CRUDViewSet):
    serializer_class = PBSerializer
    queryset = Publicity_bottom.objects.all()

    def destroy(self, request, pk):
        publicity = Publicity_bottom.objects.get(id=pk)
        os.remove(publicity.image.path)
        return super().destroy(request, pk)





