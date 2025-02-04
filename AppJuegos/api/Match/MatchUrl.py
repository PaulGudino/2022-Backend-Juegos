from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Match.MatchApiviews import (
    MatchViewSet,
    MatchFilter,
    MatchFilterHistory
)

router = DefaultRouter()
router.register(r'match', MatchViewSet, basename='match')

urlpatterns = router.urls + [ 
    path('matchfilter/', MatchFilter.as_view(), name='matchfilter'),
    path('matchfilterhistory/', MatchFilterHistory.as_view(), name='matchfilterhistory'),
]