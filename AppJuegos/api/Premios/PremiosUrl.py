from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Premios.PremiosApiviews import (
    PremiosViewSet,
    PremiosFilterbyGame
)

router = DefaultRouter()
router.register(r'premios', PremiosViewSet, basename='premios')

urlpatterns = router.urls + [
    path('premiosfilterbygame/', PremiosFilterbyGame.as_view(), name='premiosfilterbygame'),
]

