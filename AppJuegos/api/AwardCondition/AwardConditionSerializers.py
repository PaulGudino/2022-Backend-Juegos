from dataclasses import field
from rest_framework import serializers
from AppJuegos.models import (
    AwardCondition,
)
from django.utils import timezone

class AwardConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCondition
        fields= '__all__'

    def validate_start_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")
        return value

    def validate_end_date(self, value):
        if value < timezone.now().date():
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")

        if value < self.initial_data['start_date']:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
        return value

    def validate_amount(self, value):
        if value < 1:
            raise serializers.ValidationError("El monto debe ser mayor a 0")
        return value