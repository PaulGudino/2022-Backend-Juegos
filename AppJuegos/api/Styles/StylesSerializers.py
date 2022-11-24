from rest_framework import serializers
from AppJuegos.models import (
    Styles,
)

class StylesSerializers(serializers.ModelSerializer):
      class Meta:
            model = Styles
            fields= '__all__'
