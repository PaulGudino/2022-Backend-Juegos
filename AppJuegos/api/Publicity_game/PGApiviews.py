import os
from AppJuegos.models import (
    Publicity_game,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Publicity_game.PGSerializers import (
    PGSerializer
)
from rest_framework import status
from rest_framework.response import Response

class PGViewSet(CRUDViewSet):
    serializer_class = PGSerializer
    queryset = Publicity_game.objects.all()
   
    def update(self, request, pk):
        publicity = Publicity_game.objects.get(id=pk)
        new_image = request.data.get('image')
        if new_image:
            serializer = PGSerializer(publicity, data=request.data)
            if serializer.is_valid():
                old_image = publicity.image
                if old_image:
                    os.remove(old_image.path)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = PGSerializer(publicity, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PGListViewSet(OnlyListViewSet):
    serializer_class = PGSerializer
    queryset = Publicity_game.objects.all()





