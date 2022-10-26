import os
from AppJuegos.models import (
    Award,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Award.AwardSerializers import (
    AwardSerializer,
    AwardSerializerCreate,
    AwardSerializerUpdateImage,
    AwardSerializerUpdateSinImage,
    AwarderializerList,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend



class AwardViewSet(CRUDViewSet):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()

    def create(self, request):
        serializer = AwardSerializerCreate(data=request.data)
        if serializer.is_valid():
            current_stock = serializer.validated_data['initial_stock']
            serializer.save(current_stock=current_stock)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        premio = Award.objects.get(id=pk)
        new_image = request.data.get('imagen')
        if new_image:
            serializer = AwardSerializerUpdateImage(premio, data=request.data)
            if serializer.is_valid():
                current_stock = serializer.validated_data['initial_stock']
                serializer.save(current_stock=current_stock)
                old_image = premio.imagen
                print(old_image.url)
                os.remove(old_image.path)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = AwardSerializerUpdateSinImage(premio, data=request.data)
            if serializer.is_valid():
                current_stock = serializer.validated_data['initial_stock']
                serializer.save(current_stock=current_stock)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AwardListViewSet(OnlyListViewSet):
    serializer_class = AwarderializerList
    queryset = Award.objects.all()

class AwardFilterbyGame(generics.ListAPIView):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['juego']





