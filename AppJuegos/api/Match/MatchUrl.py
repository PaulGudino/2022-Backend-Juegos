from rest_framework.routers import DefaultRouter
from AppJuegos.api.Match.MatchApiviews import (
    MatchViewSet,
)

router = DefaultRouter()
router.register(r'match', MatchViewSet, basename='match')

urlpatterns = router.urls