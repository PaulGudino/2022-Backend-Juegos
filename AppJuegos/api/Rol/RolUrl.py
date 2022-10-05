from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.Rol.RolApiviews import (
    RolViewSet,
    RolPermissionViewSet,
    RolPermissionFilter,
    RolFilter
)

router = DefaultRouter()
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'rolpermission', RolPermissionViewSet, basename='rolpermission')


urlpatterns = router.urls + [ 
    path('rolpermissionfilter/', RolPermissionFilter.as_view(), name='rolpermissionfilter'),
    path('rolfilter/', RolFilter.as_view(), name='rolfilter'), 
]




