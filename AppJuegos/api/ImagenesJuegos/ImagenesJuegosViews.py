
from AppJuegos.models import ImagenesJuegos
from AppJuegos.api.ImagenesJuegos.ImagenesJuegosSerializers import ImagenesJuegosSerializer
from rest_framework.response import Response
from rest_framework import status
from AppJuegos.api.general_api import CRUDViewSet

class ImagenesJuegosViewSet(CRUDViewSet):
    serializer_class = ImagenesJuegosSerializer
    queryset = ImagenesJuegos.objects.all()

    def get_permissions(self):
        return [] 

    

    