from dataclasses import field
from xml.etree.ElementInclude import include
from rest_framework import serializers
from AppJuegos.models import (
    Premios,
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
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modify': instance.user_modify.names + ' ' + instance.user_modify.surnames if instance.user_modify else None,
            'category': instance.category,
        }

class PremiosSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id', 'name', 'description', 'image', 'initial_stock', 'is_active', 'user_register', 'category')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value
   

class PremiosSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id', 'name', 'description', 'image', 'initial_stock', 'is_active', 'user_modify', 'category')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

