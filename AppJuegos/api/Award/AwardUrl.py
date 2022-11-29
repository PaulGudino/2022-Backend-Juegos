from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Award.AwardApiviews import (
    AwardViewSet,
    AwardListViewSet,
    AwardFilter,
    AwardFilterMultiple
)

router = DefaultRouter()
router.register(r'award', AwardViewSet, basename='Award')
router.register(r'awardlist', AwardListViewSet, basename='Awardlist')
router.register(r'awardfiltermultiple', AwardFilterMultiple, basename='AwardFilterMultiple')

urlpatterns = router.urls + [
    path('awardfilter/', AwardFilter.as_view(), name='awardfilter'),
]

