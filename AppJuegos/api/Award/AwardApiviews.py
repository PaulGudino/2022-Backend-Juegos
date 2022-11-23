import os
from AppJuegos.models import (
    Award,
)
from AppJuegos.api.general_api import CRUDViewSet, OnlyListViewSet
from AppJuegos.api.Award.AwardSerializers import (
    AwardSerializer,
    AwardSerializerCreate,
    AwardSerializerUpdateImage,
    AwardSerializerUpdateSinImage,
    AwarderializerList,
)
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter

from AppJuegos.api.ValidateInformation import (
    ValidateAwardRelationships,
)

class AwardViewSet(CRUDViewSet):
    serializer_class = AwardSerializer
    queryset = Award.objects.all()

    def create(self, request):
        serializer = AwardSerializerCreate(data=request.data)
        if serializer.is_valid():
            current_stock = serializer.validated_data['initial_stock']
            serializer.save(current_stock=current_stock)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        premio = Award.objects.get(id=pk)
        new_image = request.data.get('imagen')
        if new_image:
            serializer = AwardSerializerUpdateImage(premio, data=request.data)
            if serializer.is_valid():
                amount = serializer.validated_data['initial_stock']
                diference_stock = abs(premio.initial_stock - amount)
                actual_stock = premio.initial_stock
                if amount < actual_stock:
                    premio.initial_stock = premio.initial_stock - diference_stock
                    premio.current_stock = premio.current_stock - diference_stock
                    if premio.current_stock < 0:
                        error_message = {'error': 'Tienes premios reservados, el stock inicial no puede ser menor al stock reservado'}
                        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
                    premio.save()
                elif amount > actual_stock:
                    premio.initial_stock = premio.initial_stock + diference_stock
                    premio.current_stock = premio.current_stock + diference_stock
                    premio.save()  
                old_image = premio.imagen
                os.remove(old_image.path)
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            serializer = AwardSerializerUpdateSinImage(premio, data=request.data)
            if serializer.is_valid():
                amount = serializer.validated_data['initial_stock']
                diference_stock = abs(premio.initial_stock - amount)
                actual_stock = premio.initial_stock
                if amount < actual_stock:
                    premio.initial_stock = premio.initial_stock - diference_stock
                    premio.current_stock = premio.current_stock - diference_stock
                    if premio.current_stock < 0:
                        error_message = {'error': 'Tienes premios reservados, el stock inicial no puede ser menor al stock reservado'}
                        return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
                    premio.save()
                elif amount > actual_stock:
                    premio.initial_stock = premio.initial_stock + diference_stock
                    premio.current_stock = premio.current_stock + diference_stock
                    premio.save()  
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        if ValidateAwardRelationships(pk).validate():
            award = self.get_object()
            award.is_active = False
            award.save()
            return Response({'error': 'No puedes eliminar este premio porque tiene elementos asociados, el premio se desactivará'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

class AwardListViewSet(OnlyListViewSet):
    serializer_class = AwarderializerList
    queryset = Award.objects.all()

class AwardFilter(generics.ListAPIView):
    serializer_class = AwarderializerList
    queryset = Award.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['name', 'game']
    filterset_fields = ['is_active']
    ordering_fields = ['created', 'updated']





