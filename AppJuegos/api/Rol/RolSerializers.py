from rest_framework import serializers
from AppJuegos.models import (
    Rol,
    RolPermission
)



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

class RolPermissionSerializer(serializers.ModelSerializer):

    class Meta:
        model = RolPermission
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'rol': instance.rol.name,
            'id_permission': instance.permission.id,
            'permission': instance.permission.name
        }

class CustomRolPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolPermission
        fields = ('id', 'rol', 'permission')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'rol': instance.rol.id,
            'id_permission': instance.permission.id,
            'permission': instance.permission.name
        }






