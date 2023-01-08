from AppJuegos.models import (
    Ticket,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Ticket.TicketSerializers import (
    TicketSerializer,
    TicketSerializerCreate,
    TicketSerializerUpdate,
    StateTicket
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from AppJuegos.api.ValidateInformation import (
    ValidateTicketInvoice
)
from rest_framework.decorators import action 

class TicketViewSet(CRUDViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def create(self, request):
        serializer = TicketSerializerCreate(data=request.data)

        error_ticket_message = ValidateTicketInvoice().validate(request.data.get('invoice_number'),request.data.get('client'))

        if error_ticket_message:
            return Response(error_ticket_message, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        ticket = Ticket.objects.get(id=pk)
        if ticket.state =='Reclamado':
            return Response({'No se puede eliminar un ticket ya reclamado'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, pk)

    @action(detail=True, methods=['post'])
    def change_state(self, request ,pk):
        ticket = self.get_object()
        state_serializer = StateTicket(data=request.data)
        if state_serializer.is_valid():
            ticket.state ='Reclamado'
            ticket.save()
            return Response({'message':"Se cambio el estado del ticket"},status=status.HTTP_200_OK)
        return Response(state_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketFilter(generics.ListAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'date_created', 'state',]
    filterset_fields = ['id','state','qr_code_digits']
    ordering_fields = [ 'date_created', ]