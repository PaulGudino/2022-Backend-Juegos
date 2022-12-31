from rest_framework import serializers
from AppJuegos.models import (
    Client,
)

class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        exclude = ('created','modified')

    def to_representation(self, instance):
        return {
            'id': instance.id,
            'cedula': instance.cedula,
            'names': instance.names,
            'surnames': instance.surnames,
            'email': instance.email,
            'phone': instance.phone,
            'sex': instance.sex,
            'address': instance.address,
            'created': instance.created.strftime('%d/%m/%Y %H:%M:%S'),
            'modified': instance.modified.strftime('%d/%m/%Y %H:%M:%S'),
            'user_client_register': instance.user_client_register.names + ' ' + instance.user_client_register.surnames,
            'user_client_modify':instance.user_client_modify.names + ' ' + instance.user_client_modify.surnames if instance.user_client_modify else None,
            # 'state': instance.state,
            'client': instance.cedula + ' ' + instance.names + ' ' +instance.surnames
        }

class ClientSerializerCreate(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'cedula', 'names', 'surnames', 'email', 'phone', 'sex', 'address', 'user_client_register', 'user_client_modify')
   
class ClientSerializerUpdate(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'cedula', 'names', 'surnames', 'email', 'phone', 'sex', 'address', 'user_client_modify')