import os
from AppJuegos.models import (
    TicketConfiguration,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.TicketConfiguration.TicketConfigurationSerializers import (
    TicketConfigurationSerializer,
    TicketConfigurationUpdateNotImageSerializer,
)
from rest_framework import status
from rest_framework.response import Response


class TicketConfigurationViewSet(CRUDViewSet):
    serializer_class = TicketConfigurationSerializer
    queryset = TicketConfiguration.objects.all()

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        ticket_configuration = TicketConfiguration.objects.get(id=pk)

        new_image = request.data.get('logo')
        print(new_image)
        if new_image:
            serializer = TicketConfigurationSerializer(ticket_configuration, data=request.data)
            if serializer.is_valid():
                if ticket_configuration.logo == '':
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
                else:
                    old_image = ticket_configuration.logo
                    os.remove(old_image.path)
                    serializer.save()
                    return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = TicketConfigurationUpdateNotImageSerializer(ticket_configuration, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)