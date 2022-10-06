from rest_framework.routers import DefaultRouter
from AppJuegos.api.Premios.PremiosApiviews import (
    PremiosViewSet,
    PremiosCreateViewSet,
)

router = DefaultRouter()
router.register(r'premios', PremiosViewSet, basename='premios')
router.register(r'create/premios', PremiosCreateViewSet, basename='createpremios')

urlpatterns = router.urls 

