from rest_framework.routers import DefaultRouter
from AppJuegos.api.Publicity.PublicityApiviews import (
    PublicityViewSet,
)

router = DefaultRouter()
router.register(r'publicity', PublicityViewSet, basename='publicity')

urlpatterns = router.urls