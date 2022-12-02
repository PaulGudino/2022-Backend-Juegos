from rest_framework import serializers
from AppJuegos.models import (
    Publicity_game,
)

class PGSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publicity_game
        fields = '__all__'


class PGSerializerList(serializers.ModelSerializer):
    class Meta:
        model = Publicity_game
        fields = '__all__'
  
class PGSerializerUpdateImage(serializers.ModelSerializer):
    class Meta:
        model = Publicity_game
        fields = '__all__'

class PGSerializerUpdateNoImage(serializers.ModelSerializer):
    class Meta:
        model = Publicity_game
        fields = '__all__'