from rest_framework.routers import DefaultRouter
from AppJuegos.api.Probabilidad.ProbabilidadApiviews import (
    ProbabilidadViewSet,
)

router = DefaultRouter()
router.register(r'probabilidad', ProbabilidadViewSet, basename='probabilidad')

urlpatterns = router.urls