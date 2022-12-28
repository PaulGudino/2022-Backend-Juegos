from rest_framework import serializers
from AppJuegos.models import (
    TicketConfiguration,
)

class TicketConfigurationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketConfiguration
        fields= '__all__'

class TicketConfigurationUpdateNotImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketConfiguration
        exclude = ('logo',)