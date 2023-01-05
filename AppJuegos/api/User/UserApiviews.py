from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter, OrderingFilter
from AppJuegos.models import (
    User
)
from AppJuegos.api.general_api import CRUDViewSet
from rest_framework import generics
from rest_framework.decorators import action 
from AppJuegos.api.User.UserSerializers import  (
    UserCreateSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer,
)

from AppJuegos.api.ValidateInformation import (
    ValidateUserRelationships,
    ValidateUserinClient,
)

class UserViewSet(CRUDViewSet):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def create(self, request):
        serializer = UserCreateSerializer(data=request.data)
        if (request.data.get('rol_request') != '1'):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)
        
        ValidateUserinClient().cedula(request.data.get('cedula'))
        ValidateUserinClient().email(request.data.get('email'))
        error_user_message = ValidateUserinClient().validate()
        if error_user_message:
            return Response(error_user_message, status=status.HTTP_400_BAD_REQUEST)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, pk):
        if (request.data.get('rol_request') != '1'):
            return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

        ValidateUserinClient().cedula(request.data.get('cedula'))
        ValidateUserinClient().email(request.data.get('email'))
        error_user_message = ValidateUserinClient().validate()
        if error_user_message:
            return Response(error_user_message , status=status.HTTP_400_BAD_REQUEST)

        if int(pk) == 1:
            return Response({'error': 'No puedes modificar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, pk)

    def destroy(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes eliminar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)

        if ValidateUserRelationships(pk).validate():
            user = self.get_object()
            user.is_active = False
            user.save()
            return Response({'error': 'No puedes eliminar el usuario porque tiene campos asociados, el usuario se desactivará'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return super().destroy(request, pk)

    # @action(detail=True, methods=['post'])
    # def activate_user(self, request, pk):
    #     user = self.get_object()
    #     user.is_active = True
    #     user.save()
    #     return Response(status=status.HTTP_204_NO_CONTENT)


    @action(detail=True, methods=['post'])
    def change_password(self, request, pk=None):
        user = self.get_object()
        change_serializer = ChangePasswordSerializer(data=request.data)
        if change_serializer.is_valid():
            if not user.check_password(change_serializer.data.get("old_password")):
                return Response({"old_password": ["La contraseña es incorrecta"]}, status=status.HTTP_400_BAD_REQUEST)
            user.set_password(change_serializer.data.get("new_password"))
            user.save()
            return Response({'message': "La contraseña se actualizo correctamente"},status=status.HTTP_200_OK)
        return Response(change_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserFilter(generics.ListAPIView):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend, OrderingFilter]
    search_fields = ['username', 'surnames', 'email', 'cedula']
    filterset_fields = ['rol', 'is_active']
    ordering_fields = ['created', 'updated']





