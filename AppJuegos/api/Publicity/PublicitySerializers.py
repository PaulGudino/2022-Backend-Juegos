from rest_framework import serializers
from AppJuegos.models import (
    Publicity,
)

class PublicitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields= '__all__'


class PublicitySerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields = ('id', 'image', 'titulo','created', 'modified', 'is_active')
        

class PublicitySerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields = ('id', 'image', 'titulo','created', 'modified', 'is_active')


   