from AppJuegos.models import (
    Match,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Match.MatchSerializers import (
    MatchSerializers,
)

from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from AppJuegos.models import (
    Ticket,
)


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
