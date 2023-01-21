from rest_framework import serializers
from AppJuegos.models import (
    Match,
)

class MatchSerializers(serializers.ModelSerializer):
      class Meta:
            model = Match
            fields= '__all__'

class DeliveredSerializer(serializers.Serializer):
    delivery = serializers.BooleanField(default=False)

    def validate_state(self, value):
        if value is False:
            raise serializers.ValidationError("No se entrego el premio")
        return value

class MatchHistory(serializers.ModelSerializer):
    class Meta:
        model = Match
        fields= '__all__'

    def to_representation(self, instance):
        return {
            'id':instance.id,
            'ticket': instance.ticket.id,
            'win_match': instance.win_match,
            'win_award_id': instance.award.id if instance.award else None,
            'win_award': instance.award.name if instance.award else None,
            'win_award_category': instance.award.category if instance.award else None,
            'delivered_award': instance.delivered,
            'game_selected': instance.ticket.game.name,
            'emision_date_ticket': instance.ticket.date_created.strftime('%d/%m/%Y %H:%M:%S'),
            'emision_date_match': instance.date_created.strftime('%d/%m/%Y %H:%M:%S'),
            'game_date': instance.ticket.date_ticket_played.strftime('%d/%m/%Y %H:%M:%S'),
            'user_register_ticket': instance.ticket.user_register.names + ' ' +  instance.ticket.user_register.surnames ,
            'client_player': instance.ticket.client.names + ' '+ instance.ticket.client.surnames,
            'qr':instance.ticket.qr_code_digits,
            'invoice_number':instance.ticket.invoice_number
        }

   