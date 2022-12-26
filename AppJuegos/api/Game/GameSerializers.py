# from rest_framework import serializers
# from AppJuegos.models import (
#     Game,
#     AwardCondition,
# )
# from django.utils import timezone
# from datetime import datetime

# class GameSerializers(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields= '__all__'

#     def to_representation(self, instance):
#         return {
#             'id': instance.id,
#             'name': instance.name,
#             'description': instance.description,
#             'start_date': instance.start_date.strftime('%d/%m/%Y %H:%M:%S'),
#             'end_date': instance.end_date.strftime('%d/%m/%Y %H:%M:%S'),
#             'is_active': instance.is_active,
#             'players': instance.players,
#             'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
#             'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
#             'user_register': instance.user_game_register.names + ' ' + instance.user_game_register.surnames,
#             'user_modify': instance.user_game_modify.names + ' ' + instance.user_game_modify.surnames if instance.user_game_modify else None,
#         }   


# class GameSerializerCreate(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = ('id', 'start_date', 'end_date', 'game', 'user_game_register', 'user_game_modify',)

#     def validate_start_date(self, value):
#         if value <= timezone.now():
#             raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")

#         return value

#     def validate_end_date(self, value):
#         if value <= timezone.now():
#             raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")
                
#         if len(self.initial_data['start_date']) == 19:
#             start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
#         else:
#             start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')
        
#         if value < start_date:
#             raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
#         return value
        

# class GameSerializerUpdate(serializers.ModelSerializer):
#     class Meta:
#         model = Game
#         fields = ('id', 'start_date', 'end_date', 'game', 'is_active', 'user_game_modify',)

#     def validate_start_date(self, value):
#         if value <= timezone.now():
#             raise serializers.ValidationError("La fecha de inicio debe ser mayor a la fecha actual")

#         return value

#     def validate_end_date(self, value):
#         if value <= timezone.now():
#             raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha actual")

#         if len(self.initial_data['start_date']) == 19:
#             start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
#         else:
#             start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')
        
#         if value <= start_date:
#             raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
#         return value

   

from rest_framework import serializers
from AppJuegos.models import (
    Game,
)
from django.utils import timezone
from datetime import datetime

class GameSerializers(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields= '__all__'


class GameSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'game',)

    # def validate_end_date(self, value):
                
    #     if len(self.initial_data['start_date']) == 19:
    #         start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
    #     else:
    #         start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')
        
    #     if value < start_date:
    #         raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
    #     return value    

class GameSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ('id', 'start_date', 'end_date', 'game', 'is_active',)

    # def validate_end_date(self, value):

    #     if len(self.initial_data['start_date']) == 19:
    #         start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M:%S')
    #     else:
    #         start_date = datetime.strptime(self.initial_data['start_date'].replace('T', ' '), '%Y-%m-%d %H:%M')
        
    #     if value <= start_date:
    #         raise serializers.ValidationError("La fecha de fin debe ser mayor a la fecha de inicio")
    #     return value