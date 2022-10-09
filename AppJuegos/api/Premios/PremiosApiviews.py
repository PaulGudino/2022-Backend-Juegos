import os
from AppJuegos.models import (
    Premios,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Premios.PremiosSerializers import (
    PremiosSerializer,
    PremiosSerializerCreate,
    PremiosSerializerUpdateImage,
    PremiosSerializerUpdateSinImage,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class PremiosViewSet(CRUDViewSet):
    serializer_class = PremiosSerializer
    queryset = Premios.objects.all()

    def create(self, request):
        serializer = PremiosSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        premio = Premios.objects.get(id=pk)
        new_image = request.data.get('imagen')
        if new_image:
            serializer = PremiosSerializerUpdateImage(premio, data=request.data)
            if serializer.is_valid():
                old_image = premio.imagen
                print(old_image.url)
                os.remove(old_image.path)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = PremiosSerializerUpdateSinImage(premio, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PremiosFilterbyGame(generics.ListAPIView):
    serializer_class = PremiosSerializer
    queryset = Premios.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['juego']





