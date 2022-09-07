from rest_framework.routers import DefaultRouter
from AppJuegos.api.api import (
    UserViewSet,
    RolViewSet,
    PermissionViewSet,
    RolPermissionViewSet
)

router = DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'rol', RolViewSet)
router.register(r'permission', PermissionViewSet)
router.register(r'rolpermission', RolPermissionViewSet)

urlpatterns = router.urls