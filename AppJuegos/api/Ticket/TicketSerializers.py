from rest_framework import serializers
from AppJuegos.models import (
    Ticket,
)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ('date_created','date_ticket_played')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'invoice_number': instance.invoice_number,
            'date_created': instance.date_created.strftime('%d/%m/%Y %H:%M:%S'),
            'date_ticket_played': instance.date_ticket_played.strftime('%d/%m/%Y %H:%M:%S'),
            'qr_code_digits': instance.qr_code_digits,
            'state': instance.state,
            'client': instance.client.names + ' ' + instance.client.surnames,
            'game_id': instance.game.id,
            'game_name': instance.game.name,
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'client_cedula': instance.client.cedula,
            'client_id': instance.client.id,
            'game_start' : instance.game_start.strftime('%d/%m/%Y %H:%M:%S'),
            'game_end' : instance.game_end.strftime('%d/%m/%Y %H:%M:%S'),
            'date_created_nf': instance.date_created,
        }

class TicketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'invoice_number', 'qr_code_digits', 'state', 'client', 'game', 'user_register','game_start','game_end')

class StateTicket(serializers.Serializer):
    state = serializers.BooleanField(default=False)

    def validate_state(self, value):
        if value is False:
            raise serializers.ValidationError("No se cambió el estado del ticket")
        return value