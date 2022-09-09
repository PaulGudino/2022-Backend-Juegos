from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from AppJuegos.api.serializers import CustomTokenObtainPairSerializer, CustomUserSerializer, CustomRolPermissionSerializer
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from AppJuegos.models import User

class Login(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

    def post(self, request, *args, **kwargs):
        username = request.data.get('username', None)
        password = request.data.get('password', None)
        user = authenticate(username=username, password=password)

        if user :
            login_serializer = self.get_serializer(data=request.data)
            if login_serializer.is_valid():
                user_serializer = CustomUserSerializer(user)
                permisos_serializer = CustomRolPermissionSerializer(user.rol.rolpermission_set.all(), many=True)
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'permisos': permisos_serializer.data,
                    'message': 'Login Successful'
                }, status=status.HTTP_200_OK)
            return Response({'error':'The username or password are incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'The username or password are incorrect'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):
    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('id', None))
        if user.exists():
            RefreshToken.for_user(user.first())
            return Response({'message':'Logout Successful'}, status=status.HTTP_200_OK)
        return Response({'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)




