from rest_framework import serializers
from AppJuegos.models import (
    Ticket,
)

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        exclude = ('date_created','date_modified')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'invoice_number': instance.invoice_number,
            'qr_code': instance.qr_code,
            'state': instance.state,
            'client': instance.client.names + ' ' + instance.client.surnames,
            'game': instance.game.names,
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modifier':instance.user_modifier.names + ' ' + instance.user_modifier.surnames if instance.user_modifier else None,
        }

class TicketSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'invoice_number', 'qr_code', 'state', 'client', 'client', 'game', 'user_register')
   
class TicketSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ('id', 'invoice_number', 'qr_code', 'state', 'client', 'client', 'game', 'user_modifier')