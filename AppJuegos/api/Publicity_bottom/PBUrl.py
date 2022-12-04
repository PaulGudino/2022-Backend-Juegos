from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Publicity_bottom.PBApiviews import (
    PBViewSet,
)

router = DefaultRouter()
router.register(r'Publicity_bottom', PBViewSet, basename='Publicity_bottom')

urlpatterns = router.urls
