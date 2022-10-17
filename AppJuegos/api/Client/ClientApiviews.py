import os
from AppJuegos.models import (
    Client,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Client.ClientSerializers import (
    ClientSerializer,
    ClientSerializerCreate,
    ClientSerializerUpdate,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

class ClientViewSet(CRUDViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def create(self, request):
        serializer = ClientSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        client = Client.objects.get(id = pk)
        serializer = ClientSerializerUpdate(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)