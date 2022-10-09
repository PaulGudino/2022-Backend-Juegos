from AppJuegos.models import ImagenesJuegos
from AppJuegos.api.ImagenesJuegos.ImagenesJuegosSerializers import ImagenesJuegosSerializer
from AppJuegos.api.general_api import CRUDViewSet

class ImagenesJuegosViewSet(CRUDViewSet):
    serializer_class = ImagenesJuegosSerializer
    queryset = ImagenesJuegos.objects.all()

    def get_permissions(self):
        return [] 

    