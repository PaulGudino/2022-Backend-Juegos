from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.AwardCondition.AwardConditionApiviews import (
    AwardConditionViewSet,
)

router = DefaultRouter()
router.register(r'awardcondition', AwardConditionViewSet, basename='AwardCondition')

urlpatterns = router.urls