from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Award.AwardApiviews import (
    AwardViewSet,
    AwardFilterbyGame,
    AwardListViewSet
)

router = DefaultRouter()
router.register(r'Award', AwardViewSet, basename='Award')
router.register(r'Awardlist', AwardListViewSet, basename='Awardlist')

urlpatterns = router.urls + [
    path('Awardfilterbygame/', AwardFilterbyGame.as_view(), name='Awardfilterbygame'),
]

