import os
from AppJuegos.models import (
    Publicity_top,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Publicity_top.PTSerializers import (
    PTSerializer,
)

class PTViewSet(CRUDViewSet):
    serializer_class = PTSerializer
    queryset = Publicity_top.objects.all()

    def destroy(self, request, pk):
        publicity = Publicity_top.objects.get(id=pk)
        os.remove(publicity.image.path)
        return super().destroy(request, pk)





