from rest_framework import serializers
from AppJuegos.models import (
    User,
)


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created','modified', 'is_active')
    
    def validate_phone(self, value):
        if value.isnumeric():
            return value
        else:
            raise serializers.ValidationError("El telefono debe ser númerico")

    def validate_cedula(self, value):
        if User.objects.filter(cedula=value).exists():
            raise serializers.ValidationError("La cedula ya existe")

        if value.isnumeric():
            return value
        else:
            raise serializers.ValidationError("La cedula debe ser númerico")

    def validate_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return value

    def create(self, validated_data):
        user = User(**validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user

    def to_representation(self, instance):
        return {
            'cedula': instance.cedula,
            'rol': instance.rol.name,
        }

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('created','modified','password',)
        
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
        }

class ChangePasswordSerializer(serializers.Serializer):

    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return value

    def validate_confirm_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("La contraseña debe tener al menos 8 caracteres")
        return value

    def validate(self, data):
        if data['new_password'] != data['confirm_password']:
            raise serializers.ValidationError("Las nuevas contraseñas no coinciden")
        return data


