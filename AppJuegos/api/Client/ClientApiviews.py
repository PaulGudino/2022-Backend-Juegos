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
    ValidateClientinUser
)

class ClientViewSet(CRUDViewSet):
    serializer_class = ClientSerializer
    queryset = Client.objects.all()

    def create(self, request):

        ValidateClientinUser().cedula(request.data.get('cedula'))
        ValidateClientinUser().email(request.data.get('email'))
        error_client_message = ValidateClientinUser().validate()
        print(error_client_message)
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