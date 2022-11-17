from AppJuegos.models import (
    AwardCondition,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.AwardCondition.AwardConditionSerializers import (
    AwardConditionSerializer
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

class AwardConditionViewSet(CRUDViewSet):
    serializer_class = AwardConditionSerializer
    queryset = AwardCondition.objects.all()

class AwardConditionFilter(generics.ListAPIView):
    serializer_class = AwardConditionSerializer
    queryset = AwardCondition.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id']
    filterset_fields = ['is_active']
    ordering_fields = ['start_date', 'end_date']