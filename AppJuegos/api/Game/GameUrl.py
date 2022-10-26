from rest_framework.routers import DefaultRouter
from AppJuegos.api.Game.GameApiviews import (
    GameViewSet,
)

router = DefaultRouter()
router.register(r'game', GameViewSet, basename='game')

urlpatterns = router.urls