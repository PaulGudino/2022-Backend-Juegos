# from AppJuegos.models import (
#     Game,
#     AwardCondition,
#     Award,
# )
# from AppJuegos.api.general_api import CRUDViewSet
# from AppJuegos.api.Game.GameSerializers import (
#     GameSerializers,
#     GameSerializerCreate,
#     GameSerializerUpdate,
# )

# from rest_framework import status
# from rest_framework.response import Response

# from AppJuegos.api.ValidateInformation import (
#     ValidateGameRelationships,
#     ValidateAwardConditionDateinGame
# )

# class GameViewSet(CRUDViewSet):
#     serializer_class = GameSerializers
#     queryset = Game.objects.all()

#     def create(self, request):

#         is_active = True
#         game = Game.objects.filter(is_active=is_active)
#         len_games = len(game)

#         if len_games > 0:
#             return Response("Ya existe un juego activo", status=status.HTTP_400_BAD_REQUEST)

#         serializer = GameSerializerCreate(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def update(self, request, pk):
#         game = Game.objects.get(id=pk)
#         serializer = GameSerializerUpdate(game, data=request.data)
#         if serializer.is_valid():
#             print(request.data.get('start_date'))
#             error_message = ValidateAwardConditionDateinGame().validate(pk, request.data.get('start_date'), request.data.get('end_date'))
#             if error_message:
#                 return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, pk=None):

#         game = Game.objects.get(id=pk)
#         if game.is_active == False:
#             return Response("No se puede eliminar un juego finalizado", status=status.HTTP_400_BAD_REQUEST)

#         if ValidateGameRelationships(pk).validate():
#             game = Game.objects.get(id=pk)
#             game.is_active = False
#             game.save()

#             awards = Award.objects.filter(game_id=pk)
#             for award in awards:
#                 award.is_past = True
#                 award.save()

#             awards_conditions = AwardCondition.objects.filter(game_id=pk)
#             for award_condition in awards_conditions:
#                 award_condition.is_past = True
#                 award_condition.save()

#             return Response("Juego desactivado", status=status.HTTP_200_OK)
#         return super().destroy(request, pk)



from AppJuegos.models import (
    Game,
)
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Game.GameSerializers import (
    GameSerializers,
    GameSerializerCreate,
    GameSerializerUpdate,
)

from rest_framework import status
from rest_framework.response import Response

from AppJuegos.api.ValidateInformation import (
    ValidateAwardConditionDateinGame
)

class GameViewSet(CRUDViewSet):
    serializer_class = GameSerializers
    queryset = Game.objects.all()

    def create(self, request):
        serializer = GameSerializerCreate(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def update(self, request, pk):
        game = Game.objects.get(id=pk)
        serializer = GameSerializerUpdate(game, data=request.data)
        if serializer.is_valid():
            error_message = ValidateAwardConditionDateinGame().validate(pk, request.data.get('start_date'), request.data.get('end_date'))
            if error_message:
                return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)