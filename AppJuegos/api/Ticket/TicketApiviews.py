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
from rest_framework import generics
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from AppJuegos.api.ValidateInformation import (
    ValidateTicketInvoice
)

class TicketViewSet(CRUDViewSet):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()

    def create(self, request):
        serializer = TicketSerializerCreate(data=request.data)

        error_ticket_message = ValidateTicketInvoice().validate(request.data.get('invoice_number'),request.data.get('client'))
        print('code',request.data.get('invoice_number'))
        print(type(request.data.get('invoice_number')))
        print('client',request.data.get('client'))
        print(type(request.data.get('client')))
        print(error_ticket_message)

        if error_ticket_message:
            return Response(error_ticket_message, status=status.HTTP_400_BAD_REQUEST)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TicketFilter(generics.ListAPIView):
    serializer_class = TicketSerializer
    queryset = Ticket.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'date_created', 'state',]
    filterset_fields = ['id','state','qr_code_digits']
    ordering_fields = [ 'date_created', ]