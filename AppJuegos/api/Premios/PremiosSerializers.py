from xml.etree.ElementInclude import include
from rest_framework import serializers
from AppJuegos.models import (
    Premios,
    User
)

class PremiosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Premios
        exclude = ('created','modified',)

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'image': instance.image.url,
            'initial_stock': instance.initial_stock,
            'current_stock': instance.current_stock,
            'prizes_awarded': instance.prizes_awarded,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'cedula_register': instance.cedula_register,
            'user_register': instance.user_register,
            'user_modify': instance.user_modify,
            'category': instance.category,
        }

class PremiosSerializerPost(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id','name','description','image', 'initial_stock', 'is_active', 'cedula_register', 'category' )

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value
   
    def validate_cedula_register(self, value):
        if not User.objects.filter(cedula=value).exists():
            raise serializers.ValidationError('El usuario que agrega el premio no existe')
        return value

class PremiosSerializerPut(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id','name','description','image', 'initial_stock', 'is_active', 'category', 'cedula_modify' )

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

