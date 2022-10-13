from rest_framework import serializers
from AppJuegos.models import ImagenesJuegos



class ImagenesJuegosSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagenesJuegos
        fields = '__all__'
    


