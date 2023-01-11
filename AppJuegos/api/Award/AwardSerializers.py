from rest_framework import serializers
from AppJuegos.models import (
    Award,
)

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Award
        exclude = ('created','modified',)

    def to_representation(self, instance):
        # juego = instance.get_juego_display()
        # category = instance.get_category_display()
        total_awards = instance.initial_stock + instance.condition_stock
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'imagen': 'http://' + self.context['request'].META['HTTP_HOST'] + instance.imagen.url,
            'initial_stock': instance.initial_stock,
            'condition_stock': instance.condition_stock,
            'prizes_awarded': instance.prizes_awarded,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modify': instance.user_modify.names + ' ' + instance.user_modify.surnames if instance.user_modify else None,
            'category': instance.category, 
            'game': instance.game.id,  
            'total_awards': total_awards,
        }

class AwarderializerList(serializers.ModelSerializer):
    class Meta:
        model = Award
        exclude = ('created','modified',)

    def to_representation(self, instance):
        category = instance.get_category_display()
        total_awards = instance.initial_stock + instance.condition_stock
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'imagen': 'http://' + self.context['request'].META['HTTP_HOST'] + instance.imagen.url,
            'initial_stock': instance.initial_stock,
            'condition_stock': instance.condition_stock,
            'prizes_awarded': instance.prizes_awarded,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modify': instance.user_modify.names + ' ' + instance.user_modify.surnames if instance.user_modify else None,
            'category': category,
            'game': instance.game.name,
            'total_awards': total_awards,
        }
class AwardSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_register', 'user_modify', 'category', 'game')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value
   
class AwardSerializerUpdateImage(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_modify', 'category', 'game')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

class AwardSerializerUpdateSinImage(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'initial_stock', 'is_active', 'user_modify', 'category', 'game')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

class WonAward(serializers.Serializer):
    won_award = serializers.BooleanField(default=False)

    def validate_won_award(self, value):
        if value is False:
            raise serializers.ValidationError("No se aumentó el número de premios ganados")
        return value
