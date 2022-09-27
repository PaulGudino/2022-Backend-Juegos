from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from AppJuegos.api.serializers import ( 
    CustomTokenObtainPairSerializer, 
    CustomUserSerializer, 
    ForgotPasswordSerializer,
    ResetForgotPasswordSerializer,
    LogoutSerializer
    )
from django.contrib.auth import authenticate
from rest_framework.response import Response
from rest_framework import status
from rest_framework.generics import GenericAPIView
from AppJuegos.models import User, ForgotPassword
from django.core.mail import send_mail
from django.conf import settings
import random
from django.contrib.auth.hashers import make_password

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
                return Response({
                    'token': login_serializer.validated_data.get('access'),
                    'refresh': login_serializer.validated_data.get('refresh'),
                    'user': user_serializer.data,
                    'rol': user.rol.id,
                    'message': 'Login Successful'
                }, status=status.HTTP_200_OK)
            return Response({'error':'The username or password are incorrect'}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'error':'The username or password are incorrect'}, status=status.HTTP_400_BAD_REQUEST)

class Logout(GenericAPIView):

    serializer_class = LogoutSerializer

    def post(self, request, *args, **kwargs):
        user = User.objects.filter(id=request.data.get('id', None))
        if user.exists():
            token = RefreshToken.for_user(user.first())
            token.blacklist()
            return Response({'message':'Logout Successful'}, status=status.HTTP_200_OK)
        return Response({'error':'User not found'}, status=status.HTTP_400_BAD_REQUEST)

class ForgotPasswordView(GenericAPIView):
    serializer_class = ForgotPasswordSerializer
    queryset = ForgotPassword.objects.all()

    def get_permissions(self):
        return [] 

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        user = User.objects.filter(email=email)
        email_usuario_forgot = user.first().email
        if user.exists():
            forgot_password = ForgotPassword.objects.filter(email=email_usuario_forgot)
            code = random.randint(100000, 999999)
            if forgot_password.exists():
                forgot_password.delete()
            forgot_password = ForgotPassword.objects.create(email=email_usuario_forgot, code=code)
            forgot_password.save()

            send_mail(
                'Recuperar contraseña',
                f'El codigo para recuperar tu contraseña es: {code}',
                settings.EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            return Response({'message':'Revise su email'}, status=status.HTTP_200_OK)
        return Response({'error':'El email proporcionado no existe en el sistema'}, status=status.HTTP_400_BAD_REQUEST)

class ResetForgotPasswordView(GenericAPIView):

    serializer_class = ResetForgotPasswordSerializer

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_permissions(self):
        return [] 
        

    def post(self, request, *args, **kwargs):
        email = request.data.get('email', None)
        code = request.data.get('code', None)
        password = make_password(request.data.get('password', None))
        forgot_password = ForgotPassword.objects.filter(email=email, code=code)
        if forgot_password.exists():
            user = User.objects.filter(email=email)
            user.update(password=password)
            forgot_password.delete()
            return Response({'message':'Contraseña actualizada'}, status=status.HTTP_200_OK)
        return Response({'error':'El codigo proporcionado es incorrecto o no existe'}, status=status.HTTP_400_BAD_REQUEST)

