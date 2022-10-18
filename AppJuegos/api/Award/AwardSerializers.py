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
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'imagen': 'http://' + self.context['request'].META['HTTP_HOST'] + instance.imagen.url,
            'initial_stock': instance.initial_stock,
            'current_stock': instance.current_stock,
            'prizes_awarded': instance.prizes_awarded,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modify': instance.user_modify.names + ' ' + instance.user_modify.surnames if instance.user_modify else None,
            'category': instance.category, 
            'juego': instance.juego,  
        }

class AwarderializerList(serializers.ModelSerializer):
    class Meta:
        model = Award
        exclude = ('created','modified',)

    def to_representation(self, instance):
        juego = instance.get_juego_display()
        category = instance.get_category_display()
        return {
            'id': instance.id,
            'name': instance.name,
            'description': instance.description,
            'imagen': 'http://' + self.context['request'].META['HTTP_HOST'] + instance.imagen.url,
            'initial_stock': instance.initial_stock,
            'current_stock': instance.current_stock,
            'prizes_awarded': instance.prizes_awarded,
            'is_active': instance.is_active, 
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'user_register': instance.user_register.names + ' ' + instance.user_register.surnames,
            'user_modify': instance.user_modify.names + ' ' + instance.user_modify.surnames if instance.user_modify else None,
            'category': category,
            'juego': juego,
        }
class AwardSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_register', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value
   
class AwardSerializerUpdateImage(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'imagen', 'initial_stock', 'is_active', 'user_modify', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value

class AwardSerializerUpdateSinImage(serializers.ModelSerializer):
    class Meta:
        model = Award
        fields = ('id', 'name', 'description', 'initial_stock', 'is_active', 'user_modify', 'category', 'juego')

    def validate_initial_stock(self, value):
        if value <= 0:
            raise serializers.ValidationError('El stock inicial no puede ser negativo o cero')
        return value