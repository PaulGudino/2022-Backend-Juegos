from rest_framework import serializers
from AppJuegos.models import (
    AwardCondition,
    Game
)
from django.utils import timezone
from datetime import datetime

class AwardConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCondition
        exclude = ('is_approved',)

    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")

        inicio_juego = Game.objects.get(id=self.initial_data['game']).start_date
        fin_juego = Game.objects.get(id=self.initial_data['game']).end_date

        if value < inicio_juego:
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha de inicio del juego")

        if value > fin_juego:
            raise serializers.ValidationError("La fecha de inicio debe ser menor a la fecha de fin del juego")

        return value

    def validate_end_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")

        inicio_juego = Game.objects.get(id=self.initial_data['game']).start_date
        fin_juego = Game.objects.get(id=self.initial_data['game']).end_date

        if value < inicio_juego:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio del juego")

        if value > fin_juego:
            raise serializers.ValidationError("La fecha de fin debe ser menor a la fecha de fin del juego")

        if len(self.initial_data['start_date']) == 19:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
        else:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')

        if value < start_date:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
        return value

    def to_representation(self, instance):
        duration = instance.end_date - instance.start_date
        return {
            'id': instance.id,
            'award': instance.award.id,
            'game': instance.game.name,
            'start_date': instance.start_date.strftime('%d/%m/%Y %H:%M:%S'),
            'end_date': instance.end_date.strftime('%d/%m/%Y %H:%M:%S'),
            'is_approved': instance.is_approved,
            'duration': duration.days,
            'start_date_nf': instance.start_date,
            'end_date_nf': instance.end_date,
        }

class AwardConditionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AwardCondition
        exclude = ('award','is_approved',)
        
    def validate_start_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")

        inicio_juego = Game.objects.get(id=self.initial_data['game']).start_date
        fin_juego = Game.objects.get(id=self.initial_data['game']).end_date

        if value < inicio_juego:
            raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha de inicio del juego")

        if value > fin_juego:
            raise serializers.ValidationError("La fecha de inicio debe ser menor a la fecha de fin del juego")

        return value

    def validate_end_date(self, value):
        if value < timezone.now():
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")

        inicio_juego = Game.objects.get(id=self.initial_data['game']).start_date
        fin_juego = Game.objects.get(id=self.initial_data['game']).end_date

        if value < inicio_juego:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio del juego")

        if value > fin_juego:
            raise serializers.ValidationError("La fecha de fin debe ser menor a la fecha de fin del juego")

        if len(self.initial_data['start_date']) == 19:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
        else:
            start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')

        if value < start_date:
            raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
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
            'is_approved': instance.is_approved,
        }
