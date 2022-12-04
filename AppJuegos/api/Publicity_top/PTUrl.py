from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Publicity_top.PTApiviews import (
    PTViewSet,
)

router = DefaultRouter()
router.register(r'Publicity_top', PTViewSet, basename='Publicity_top')

urlpatterns = router.urls
