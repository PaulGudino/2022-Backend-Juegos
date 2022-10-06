from AppJuegos.models import (
    Premios,
    User
)
from rest_framework.generics import GenericAPIView
from AppJuegos.api.general_api import CRUDViewSet
from AppJuegos.api.Premios.PremiosSerializers import (
    PremiosSerializer,
    PremiosSerializerPost,
    PremiosSerializerPut
)
from rest_framework import status
from rest_framework.response import Response


class PremiosViewSet(CRUDViewSet):
    serializer_class = PremiosSerializer
    queryset = Premios.objects.all()

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class PremiosCreateViewSet(CRUDViewSet):
    serializer_class = PremiosSerializerPost
    queryset = Premios.objects.all()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            cedula = request.data.get('cedula_register', None)
            current_stock = request.data.get('initial_stock', None)
            print(cedula)
            user = User.objects.filter(cedula=cedula).first()
            print(user)
            if user:
                user_register = user.names + ' ' + user.surnames
                serializer.save(user_register=user_register, current_stock=current_stock)
                return Response({'message': 'Premio registrado correctamente'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'El usuario no existe'}, status=status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)







