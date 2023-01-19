from rest_framework import serializers
from AppJuegos.models import (
    Publicity_game,
)

class PGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity_game
        fields = '__all__'
