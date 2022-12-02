from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Publicity_game.PGApiviews import (
    PGViewSet,
    PGListViewSet,
)

router = DefaultRouter()
router.register(r'Publicity_game', PGViewSet, basename='Publicity_game')
router.register(r'PGlist', PGListViewSet, basename='PGlist')

urlpatterns = router.urls
