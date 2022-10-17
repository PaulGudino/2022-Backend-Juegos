from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Premios.PremiosApiviews import (
    PremiosViewSet,
    PremiosFilterbyGame,
    PremiosListViewSet
)

router = DefaultRouter()
router.register(r'premios', PremiosViewSet, basename='premios')
router.register(r'premioslist', PremiosListViewSet, basename='premioslist')

urlpatterns = router.urls + [
    path('premiosfilterbygame/', PremiosFilterbyGame.as_view(), name='premiosfilterbygame'),
]

