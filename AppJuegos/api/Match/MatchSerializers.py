from rest_framework import serializers
from AppJuegos.models import (
    Match,
)

class MatchSerializers(serializers.ModelSerializer):
      class Meta:
            model = Match
            fields= '__all__'



   