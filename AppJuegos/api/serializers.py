from rest_framework import serializers
from AppJuegos.models import User, Rol, Permission, RolPermission
from django.utils import timezone

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    pass

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'names', 'surnames')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created','modified','last_session',)

    def validate_phone(self, value):
        if value.isnumeric():
            return value
        else:
            raise serializers.ValidationError("El telefono debe ser númerico")

    def validate_cedula(self, value):
        if value.isnumeric():
            return value
        else:
            raise serializers.ValidationError("La cedula debe ser númerico")

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'cedula': instance.cedula,
            'names': instance.names,
            'surnames': instance.surnames,
            'username': instance.username,
            'email': instance.email,
            'phone': instance.phone,
            'password': instance.password,
            'sex': instance.sex,
            'address' : instance.address,
            'rol' : instance.rol.name,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'last_session': instance.last_session.strftime('%d/%m/%Y %H:%M:%S')
        } 

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        exclude = ('created','modified',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S')
        }

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = '__all__'

class RolPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RolPermission
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'rol': instance.rol.name,
            'permission': instance.permission.name
        }

