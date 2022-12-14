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
            'client': instance.client.names,
            'game': instance.game.name,
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
        }

class TicketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'invoice_number', 'qr_code_digits', 'state', 'client', 'game', 'user_register')
   
class TicketSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'invoice_number', 'qr_code_digits', 'state', 'date_ticket_played', 'client', 'game')