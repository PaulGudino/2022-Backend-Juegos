from AppJuegos.models import (
    Match,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Match.MatchSerializers import (
    MatchSerializers,
)

from rest_framework import status
from rest_framework.response import Response

class MatchViewSet(CRUDViewSet):
    serializer_class = MatchSerializers
    queryset = Match.objects.all()

    def create(self, request):
        serializer = MatchSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        match = Match.objects.get(id=pk)
        print(request.data.get('id'))

        serializer = MatchSerializers(match, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
