from rest_framework import serializers
from AppJuegos.models import (
    Game,
)

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields= '__all__'


class GameSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'modification_date', 'game', 'is_active')
        

class GameSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'modification_date', 'game', 'is_active')

   