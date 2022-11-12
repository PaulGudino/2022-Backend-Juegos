from AppJuegos.models import (
    Game,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Game.GameSerializers import (
    GameSerializers,
    GameSerializerCreate,
    GameSerializerUpdate,
)

from rest_framework import status
from rest_framework.response import Response

class GameViewSet(CRUDViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()

    def create(self, request):
        serializer = GameSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        game = Game.objects.get(id=pk)
        print(request.data.get('id'))
        print(game)
        #new_start_date = request.data.get('start_date')

        serializer = GameSerializerUpdate(game, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

