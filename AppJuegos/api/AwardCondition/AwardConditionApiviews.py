from AppJuegos.models import (
    AwardCondition,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.AwardCondition.AwardConditionSerializers import (
    AwardConditionSerializer,
    AwardConditionFilterSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from AppJuegos.api.ValidateInformation import (
    ReduceAward
)

class AwardConditionViewSet(CRUDViewSet):
    serializer_class = AwardConditionSerializer
    queryset = AwardCondition.objects.all()

    def create(self, request):
        error_message = ReduceAward().current_stock(int(request.data['amount']), request.data['award'])
        if error_message:
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().create(request)


class AwardConditionFilter(generics.ListAPIView):
    serializer_class = AwardConditionFilterSerializer
    queryset = AwardCondition.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'start_date', 'end_date']
    filterset_fields = ['is_active']
    ordering_fields = ['start_date', 'end_date']