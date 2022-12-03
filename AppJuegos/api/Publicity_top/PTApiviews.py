import os
from AppJuegos.models import (
    Publicity_top,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Publicity_top.PTSerializers import (
    PTSerializer,
)
from rest_framework import status
from rest_framework.response import Response

class PTViewSet(CRUDViewSet):
    serializer_class = PTSerializer
    queryset = Publicity_top.objects.all()

    def destroy(self, request, pk):
        return super().destroy(request, pk)





