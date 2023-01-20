from AppJuegos.models import (
    Match,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Match.MatchSerializers import (
    MatchSerializers,
    MatchHistory,
    DeliveredSerializer
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from AppJuegos.models import (
    Ticket,
)
from rest_framework.decorators import action 

class MatchViewSet(CRUDViewSet):
    serializer_class = MatchSerializers
    queryset = Match.objects.all()

    def create(self, request):
        serializer = MatchSerializers(data=request.data)
        if serializer.is_valid():
            ticket = Ticket.objects.filter(
                id= request.data.get('ticket')
            ).first()
            ticket.state = 'Reclamado'
            ticket.save()
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    @action(detail=True, methods=['post'])
    def award_delivered(self, request ,pk):
        macth = self.get_object()
        delivered_serializer = DeliveredSerializer(data=request.data)
        if delivered_serializer.is_valid():
            macth.delivered = True
            macth.save()
            return Response({'message':"Se entrego el premio"},status=status.HTTP_200_OK)
        return Response(delivered_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

class MatchFilter(generics.ListAPIView):
    serializer_class = MatchSerializers
    queryset = Match.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['win_match', 'date_created']
    filterset_fields = {
        'win_match':['exact'],
        'date_created':['date__range'],
    }
    ordering_fields = ['win_match', 'date_created']


class MatchFilterHistory(generics.ListAPIView):
    serializer_class = MatchHistory
    queryset = Match.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    filterset_fields = {
        'ticket__client__id':['exact'],
        'win_match':['exact'],
        'delivered':['exact'],
        'date_created':['date__range'],
    }
    ordering_fields = ['date_created']
