from rest_framework import serializers
from AppJuegos.models import (
    Game,
)

class GameSerializers(serializers.ModelSerializer):
      class Meta:
            model = Game
            fields= '__all__'
