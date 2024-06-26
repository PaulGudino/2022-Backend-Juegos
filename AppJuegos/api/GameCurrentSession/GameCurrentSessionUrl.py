from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.GameCurrentSession.GameCurrentSessionApiviews import (
    GameCurrentSessionViewSet,
    GameCurrentSessionFilter,
    GameCurrentFilter,
    get_last_session,
)

router = DefaultRouter()
router.register(r'gamecurrentsession', GameCurrentSessionViewSet, basename='gamecurrentsession')

urlpatterns = router.urls + [
    path('gamecurrentsessionfilter/', GameCurrentSessionFilter.as_view(), name='GameCurrentSessionFilter'),
    path('gamecurrentsession/update_game_id/', GameCurrentSessionViewSet.as_view({'patch': 'update_game_id'}), name='update_game_id'),
    path('gamecurrentsession/get_last_session/', get_last_session, name='get_last_session'),  # Añadido para la vista de la última sesión
    path('gamecurrentsessionfilter/', GameCurrentSessionFilter.as_view(), name='GameCurrentSessionFilter'),
    path('gamecurrentfilter/', GameCurrentFilter.as_view(), name='gamecurrentfilter'),
]