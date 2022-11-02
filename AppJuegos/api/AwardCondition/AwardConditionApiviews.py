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

class AwardConditionViewSet(CRUDViewSet):
    serializer_class = AwardConditionSerializer
    queryset = AwardCondition.objects.all()