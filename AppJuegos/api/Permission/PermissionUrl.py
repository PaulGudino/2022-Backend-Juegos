from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Permission.PermissionApiviews import (
    PermissionViewSet,
    PermissionFilter
)

router = DefaultRouter()
router.register(r'permission', PermissionViewSet, basename='permission')

urlpatterns = router.urls + [
    path('permissionfilter/', PermissionFilter.as_view(), name='permissionfilter'),
]