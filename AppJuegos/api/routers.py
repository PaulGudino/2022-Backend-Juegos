from rest_framework.routers import DefaultRouter
from AppJuegos.api.api import (
    UserViewSet,
    RolViewSet,
    PermissionViewSet,
    RolPermissionViewSet
)

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'permission', PermissionViewSet, basename='permission')
router.register(r'rolpermission', RolPermissionViewSet, basename='rolpermission')

urlpatterns = router.urls