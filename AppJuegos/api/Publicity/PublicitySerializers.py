from rest_framework import serializers
from AppJuegos.models import (
    Publicity,
)

class PublicitySerializers(serializers.ModelSerializer):
    class Meta:
        model = Publicity
        fields= '__all__'



   