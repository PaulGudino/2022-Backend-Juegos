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

from AppJuegos.api.ValidateInformation import (
    ValidateClientinUser,
    ValidateClientRelationships
)
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework import generics

class ClientViewSet(CRUDViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def create(self, request):

        ValidateClientinUser().cedula(request.data.get('cedula'))
        ValidateClientinUser().email(request.data.get('email'))
        error_client_message = ValidateClientinUser().validate()
        if error_client_message:
            return Response(error_client_message, status=status.HTTP_400_BAD_REQUEST)

        serializer = ClientSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):

        ValidateClientinUser().cedula(request.data.get('cedula'))
        ValidateClientinUser().email(request.data.get('email'))
        error_client_message = ValidateClientinUser().validate()
        if error_client_message:
            return Response(error_client_message, status=status.HTTP_400_BAD_REQUEST)

        client = Client.objects.get(id = pk)
        serializer = ClientSerializerUpdate(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        if ValidateClientRelationships(pk).validate():
            return Response({'error': 'No puedes eliminar el cliente porque tiene campos asociados'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

class ClientFilter(generics.ListAPIView):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['id']
    ordering_fields = ['created', 'modified']


    