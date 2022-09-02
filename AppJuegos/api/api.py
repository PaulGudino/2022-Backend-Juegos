from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from AppJuegos.models import User, Rol, Permission, RolPermission
from AppJuegos.api.serializers import UserSerializer, RolSerializer, PermissionSerializer, RolPermissionSerializer
from AppJuegos.api.general_serializers import GeneralListApiView, GeneralRetrieveUpdateDestroyApiView, GeneralListCreateApiView


class User_ListCreate_APIView(GeneralListCreateApiView):
    serializer_class = UserSerializer
    queryset = User.objects.all()

class User_RetrieveUpdateDestroy_APIView(GeneralRetrieveUpdateDestroyApiView):
    serializer_class = UserSerializer

class Rol_ListCreate_APIView(GeneralListCreateApiView):
    serializer_class = RolSerializer
    queryset = Rol.objects.all()

class Rol_RetrieveUpdateDestroy_APIView(GeneralRetrieveUpdateDestroyApiView):
    serializer_class = RolSerializer

class Permission_List_APIView(GeneralListApiView):
    serializer_class = PermissionSerializer        

class RolPermission_ListCreate_APIView(GeneralListCreateApiView):
    serializer_class = RolPermissionSerializer
    queryset = RolPermission.objects.all()

class RolPermission_RetrieveUpdateDestroy_APIView(GeneralRetrieveUpdateDestroyApiView):
    serializer_class = RolPermissionSerializer












