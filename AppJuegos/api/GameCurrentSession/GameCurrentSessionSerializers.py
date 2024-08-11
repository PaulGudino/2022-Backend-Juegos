from rest_framework import serializers
from AppJuegos.models import (
    GameCurrentSession,
)

class GameCurrentSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCurrentSession
        fields = ('id', 'kiosko_numero', 'ticket_id', 'game_id', 'gano', 'award_id', 'fecha_hora_startgame', 'fecha_hora_finalgame')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'kiosko_numero': instance.kiosko_numero,
            'ticket_id': instance.ticket_id.id,  # Asegúrate de ajustar esto según sea necesario
            'game_id': instance.game_id,      # Asegúrate de ajustar esto según sea necesario
            'gano': instance.gano,
            'award_id': instance.award_id.id if instance.award_id else None,  # Ajustar según sea necesario
            'fecha_hora_startgame': instance.fecha_hora_startgame.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'fecha_hora_finalgame': instance.fecha_hora_finalgame.strftime('%Y-%m-%dT%H:%M:%S.%fZ') if instance.fecha_hora_finalgame else None,
        }
    

class GameCurrentSessionSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = GameCurrentSession
        fields = ('id', 'invoice_number', 'qr_code_digits', 'state', 'client', 'game', 'user_register','game_start','game_end')


class GameCurrentSessionUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCurrentSession
        fields = '__all__'

    def validate_field(self, value):
        if value < 0:
            raise serializers.ValidationError("El campo debe ser mayor o igual a cero")
        return value

class GameCurrentSessionFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = GameCurrentSession
        fields = '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'kiosko_numero': instance.kiosko_numero,
            'ticket_id': instance.ticket_id.id,  # Asegúrate de ajustar esto según sea necesario
            'game_id': instance.game_id.id,      # Asegúrate de ajustar esto según sea necesario
            'gano': instance.gano,
            'award_id': instance.award_id.id if instance.award_id else None,  # Ajustar según sea necesario
            'fecha_hora_startgame': instance.fecha_hora_startgame.strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'fecha_hora_finalgame': instance.fecha_hora_finalgame.strftime('%Y-%m-%dT%H:%M:%S.%fZ') if instance.fecha_hora_finalgame else None,
        }
