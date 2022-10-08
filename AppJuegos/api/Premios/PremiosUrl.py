from rest_framework.routers import DefaultRouter
from AppJuegos.api.Premios.PremiosApiviews import (
    PremiosViewSet,
)

router = DefaultRouter()
router.register(r'premios', PremiosViewSet, basename='premios')

urlpatterns = router.urls 

