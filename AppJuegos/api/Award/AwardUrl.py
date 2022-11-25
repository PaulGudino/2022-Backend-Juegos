from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Award.AwardApiviews import (
    AwardViewSet,
    AwardListViewSet,
    AwardFilter
)

router = DefaultRouter()
router.register(r'award', AwardViewSet, basename='Award')
router.register(r'awardlist', AwardListViewSet, basename='Awardlist')

urlpatterns = router.urls + [
    path('awardfilter/', AwardFilter.as_view(), name='awardfilter'),
]

