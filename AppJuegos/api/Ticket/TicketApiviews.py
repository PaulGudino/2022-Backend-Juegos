from AppJuegos.models import (
    Ticket,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Ticket.TicketSerializers import (
    TicketSerializer,
    TicketSerializerCreate,
    TicketSerializerUpdate,
)
from rest_framework import status
from rest_framework.response import Response

class TicketViewSet(CRUDViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def create(self, request):

        serializer = TicketSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        
        Ticket = Ticket.objects.get(id = pk)
        serializer = TicketSerializerUpdate(Ticket, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)