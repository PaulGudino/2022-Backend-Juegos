from AppJuegos.api.ImagenesJuegos.ImagenesJuegosViews import (
    ImagenesJuegosViewSet
)
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'imagenesjuegos', ImagenesJuegosViewSet, basename='imagenesjuegos')
urlpatterns = router.urls







