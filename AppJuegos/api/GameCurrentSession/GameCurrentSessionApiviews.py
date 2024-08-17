from AppJuegos.models import (
    GameCurrentSession,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.GameCurrentSession.GameCurrentSessionSerializers import (
    GameCurrentSessionSerializer,
    GameCurrentSessionSerializerCreate,
    GameCurrentSessionFilterSerializer,
    GameCurrentSessionUpdateSerializer
)

from rest_framework import status, generics
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import action, api_view
from rest_framework.viewsets import ModelViewSet
from datetime import datetime


class GameCurrentSessionViewSet(CRUDViewSet):
    serializer_class = GameCurrentSessionSerializer
    queryset = GameCurrentSession.objects.all()
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = {
        'gano': ['exact'],
        'fecha_hora_startgame': ['date__range', 'gte', 'lte'],
        'fecha_hora_finalgame': ['date__range', 'gte', 'lte'],
    }
    search_fields = ['id', 'fecha_hora_startgame']
    ordering_fields = ['fecha_hora_startgame', 'fecha_hora_finalgame', 'id']

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def update(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            serializer = self.get_serializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except GameCurrentSession.DoesNotExist:
            return Response("La sesión de juego no existe", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def destroy(self, request, *args, **kwargs):
        try:
            instance = self.get_object()
            instance.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except GameCurrentSession.DoesNotExist:
            return Response("La sesión de juego no existe", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    @action(detail=True, methods=['post'])
    def end_game(self, request, pk=None):
        try:
            instance = self.get_object()
            serializer = GameCurrentSessionUpdateSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except GameCurrentSession.DoesNotExist:
            return Response("La sesión de juego no existe", status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    @action(detail=False, methods=['patch'])
    def update_game_id(self, request):
        kiosko_numero = request.data.get('kiosko_numero')
        game_id = request.data.get('game_id')

        try:
            session = GameCurrentSession.objects.filter(kiosko_numero=kiosko_numero).latest('fecha_hora_startgame')
            session.game_id = game_id
            session.save()
            return Response({'status': 'Game ID updated successfully'}, status=status.HTTP_200_OK)
        except GameCurrentSession.DoesNotExist:
            return Response({'error': 'Game session not found'}, status=status.HTTP_404_NOT_FOUND)
        except Exception as e:
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
@api_view(['GET'])
def get_last_session(request):
    kiosko_numero = request.query_params.get('kiosko_numero')

    if not kiosko_numero:
        return Response({"error": "kiosko_numero is required."}, status=status.HTTP_400_BAD_REQUEST)

    try:
        session = GameCurrentSession.objects.filter(kiosko_numero=kiosko_numero).last()
        if not session:
            return Response({"error": "No session found for the given kiosko_numero."}, status=status.HTTP_404_NOT_FOUND)

        serializer = GameCurrentSessionSerializer(session)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    

class GameCurrentSessionFilter(generics.ListAPIView):
    serializer_class = GameCurrentSessionSerializer
    queryset = GameCurrentSession.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'date_created', 'state',]
    filterset_fields = {
        'id': ['exact'],
        'game_id': ['exact'],
        'kiosko_numero': ['exact'],
        'fecha_hora_startgame': ['date__range'],
    }
    ordering_fields = ['fecha_hora_startgame']


class GameCurrentFilter(generics.ListAPIView):
    serializer_class = GameCurrentSessionSerializer
    queryset = GameCurrentSession.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['id', 'game_id', 'kiosko_numero']
    filterset_fields = {
        'id': ['exact'],
        'game_id': ['exact'],
        'gano':['exact'],
        'kiosko_numero': ['exact'],
        'fecha_hora_startgame': ['date__range'],
    }
    ordering_fields = ['fecha_hora_startgame']