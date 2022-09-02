from rest_framework import serializers
from AppJuegos.models import User, Rol, Permission, RolPermission
from werkzeug.security import generate_password_hash



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'cedula',
            'first_name',
            'second_name',
            'father_last_name',
            'mother_last_name',
            'email',
            'phone',
            'password',
            'sex',
            'address',
            'rol',
            'state'
        ]

    def create(self, validated_data):
        user = User(**validated_data)
        user.password = generate_password_hash(user.password, 'sha256', 30)
        user.save()
        return user

    def update(self, instance, validated_data):
        user = super().update(instance, validated_data)
        user.password = generate_password_hash(user.password, 'sha256', 30)
        user.modified = timezone.now()
        user.save()
        return user

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rol
        fields = 'id', 'name', 'description', 'state'

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

