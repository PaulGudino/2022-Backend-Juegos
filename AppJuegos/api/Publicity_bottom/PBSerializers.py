from rest_framework import serializers
from AppJuegos.models import (
    Publicity_bottom,
)

class PBSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity_bottom
        fields = '__all__'