from rest_framework.routers import DefaultRouter
from AppJuegos.api.AwardGame.AwardGameApiviews import (
   AwardGameViewSet,
)

router = DefaultRouter()
router.register(r'awardGame', AwardGameViewSet, basename='award_game')

urlpatterns = router.urls