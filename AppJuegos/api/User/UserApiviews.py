
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework import status
from rest_framework.filters import SearchFilter
from AppJuegos.models import User
from AppJuegos.api.general_api import CRUDViewSet
from rest_framework import generics
from rest_framework.decorators import action 
from AppJuegos.api.User.UserSerializers import  (
    UserSerializer,
    UserUpdateSerializer,
    ChangePasswordSerializer
)


class UserCreateViewSet(CRUDViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def list(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def destroy(self, request, pk):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

class UserViewSet(CRUDViewSet):
    serializer_class = UserUpdateSerializer
    queryset = User.objects.all()

    def create(self, request):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def update(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes modificar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, pk)

    def destroy(self, request, pk):
        if int(pk) == 1:
            return Response({'error': 'No puedes eliminar el rol administrador'}, status=status.HTTP_400_BAD_REQUEST)
        return super().destroy(request, pk)

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
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['rol__name']
    filterset_fields = ['rol']





