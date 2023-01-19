from rest_framework.routers import DefaultRouter
from AppJuegos.api.Audio.AudioApiViews import (
    AudioViewSet,
)

router = DefaultRouter()
router.register(r'audio', AudioViewSet, basename='Audio')

urlpatterns = router.urls