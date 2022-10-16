from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Client.ClientApiviews import (
    ClientViewSet,
)

router = DefaultRouter()
router.register(r'client', ClientViewSet, basename='client')

urlpatterns = router.urls