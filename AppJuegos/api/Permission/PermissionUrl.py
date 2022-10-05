from rest_framework.routers import DefaultRouter
from AppJuegos.api.Permission.PermissionApiviews import (
    PermissionViewSet,
)

router = DefaultRouter()
router.register(r'permission', PermissionViewSet, basename='permission')

urlpatterns = router.urls