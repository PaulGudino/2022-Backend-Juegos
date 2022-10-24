from rest_framework.routers import DefaultRouter
from AppJuegos.api.GameDate.GameDataApiviews import (
    GameDateViewSet,
)

router = DefaultRouter()
router.register(r'gamedate', GameDateViewSet, basename='game_date')

urlpatterns = router.urls