from rest_framework import serializers
from AppJuegos.models import (
    GameDate,
)
from django.utils import timezone

class GameDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameDate
        fields = '__all__'

    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('La fecha de inicio no puede ser menor a la fecha actual')
        return value

    def validate_end_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError('La fecha de fin no puede ser menor a la fecha actual')
        return value

        




