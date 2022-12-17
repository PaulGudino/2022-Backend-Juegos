from AppJuegos.models import (
    AwardCondition,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.AwardCondition.AwardConditionSerializers import (
    AwardConditionSerializer,
    AwardConditionFilterSerializer,
    AwardConditionUpdateSerializer

)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from AppJuegos.api.ValidateInformation import (
    ReduceAwardInitialStock,
    AddAwardInitialStock,
)

class AwardConditionViewSet(CRUDViewSet):
    serializer_class = AwardConditionSerializer
    queryset = AwardCondition.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            error_message = ReduceAwardInitialStock().initial_stock(request.data.get('award'))
            if error_message:
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):

        award_condition = AwardCondition.objects.get(id=pk)
        if award_condition.is_approved == True:
            return Response({'Esta condición de premio ya fue aprobadan, no se puede editar'}, status=status.HTTP_400_BAD_REQUEST)

        serializer = AwardConditionUpdateSerializer(self.get_object(), data=request.data)
        print(serializer.is_valid())
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        
        award_condition = AwardCondition.objects.get(id=pk)
        if award_condition.is_approved == True:
            return Response({'No se puede eliminar una condición de premio ya aprobada'}, status=status.HTTP_400_BAD_REQUEST)

        AddAwardInitialStock().initial_stock(self.get_object().award.id)
        return super().destroy(request, pk)


class AwardConditionFilter(generics.ListAPIView):
    serializer_class = AwardConditionFilterSerializer
    queryset = AwardCondition.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'start_date', 'end_date']
    filterset_fields = ['is_approved']
    ordering_fields = ['start_date', 'end_date']