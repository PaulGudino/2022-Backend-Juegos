from rest_framework import serializers
from AppJuegos.models import (
    Publicity_top,
)

class PTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity_top
        fields = '__all__'