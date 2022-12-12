from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.TicketConfiguration.TicketConfigurationApiviews import (
    TicketConfigurationViewSet,
)

router = DefaultRouter()
router.register(r'ticketconfiguration', TicketConfigurationViewSet, basename='TicketConfiguration')

urlpatterns = router.urls

