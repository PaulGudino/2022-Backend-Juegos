from rest_framework import serializers
from AppJuegos.models import (
    Game,
)
class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields= '__all__'

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'start_date': instance.start_date.strftime('%d/%m/%Y %H:%M:%S'),
            'end_date': instance.end_date.strftime('%d/%m/%Y %H:%M:%S'),
            'start_date_nf': instance.start_date,
            'end_date_nf': instance.end_date,
            'players': instance.players,
            'name': instance.name,
        }


class GameSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'game',)


class GameSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'game', 'is_active',)
