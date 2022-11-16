from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Ticket.TicketApiviews import (
    TicketViewSet,
)

router = DefaultRouter()
router.register(r'ticket', TicketViewSet, basename='ticket')

urlpatterns = router.urls