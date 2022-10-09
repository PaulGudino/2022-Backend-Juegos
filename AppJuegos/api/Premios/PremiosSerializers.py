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

class PremiosSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_register', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value
   
class PremiosSerializerUpdateImage(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_modify', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

class PremiosSerializerUpdateSinImage(serializers.ModelSerializer):
    class Meta:
        model = Premios
        fields = ('id', 'name', 'description', 'initial_stock', 'is_active', 'user_modify', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value