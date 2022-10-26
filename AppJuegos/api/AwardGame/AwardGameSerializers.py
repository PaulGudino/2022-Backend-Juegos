from rest_framework import serializers
from AppJuegos.models import (
    AwardGame,
)

class AwardGameSerializers(serializers.ModelSerializer):
    class Meta:
        model = AwardGame
        fields= '__all__'
