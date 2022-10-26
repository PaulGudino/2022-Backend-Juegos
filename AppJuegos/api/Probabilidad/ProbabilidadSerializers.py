from rest_framework import serializers
from AppJuegos.models import (
    Probabilidad,
)

class ProbabilidadSerializers(serializers.ModelSerializer):
      class Meta:
            model = Probabilidad
            fields= '__all__'
