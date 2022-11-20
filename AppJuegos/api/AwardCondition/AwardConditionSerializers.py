from rest_framework import serializers
from AppJuegos.models import (
    AwardCondition,
)
from django.utils import timezone
from datetime import datetime

class AwardConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCondition
        fields= '__all__'

    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")
        return value

    def validate_end_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")

        if len(self.initial_data['start_date']) == 19:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
        else:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')

        if value < start_date:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
        return value

    def validate_amount(self, value):
        if value < 1:
            raise serializers.ValidationError("El monto debe ser mayor a 0")
        return value

class AwardConditionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCondition
        fields= '__all__'
        
    def to_representation(self, instance):
        return {
            'id': instance.id,
            'award': instance.award.name,
            'game': instance.game.name,
            'start_date': instance.start_date.strftime('%d/%m/%Y %H:%M:%S'),
            'end_date': instance.end_date.strftime('%d/%m/%Y %H:%M:%S'),
            'amount': instance.amount,
            'is_active': instance.is_active,
        }
