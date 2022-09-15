from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.api import (
    UserCreateViewSet,
    UserViewSet,
    RolViewSet,
    PermissionViewSet,
    RolPermissionViewSet,
    RolPermissionFilter,
    RolFilter,
    UserFilter,
)

router = DefaultRouter()
router.register(r'create/user', UserCreateViewSet, basename='createuser')
router.register(r'user', UserViewSet, basename='user')
router.register(r'rol', RolViewSet, basename='rol')
router.register(r'permission', PermissionViewSet, basename='permission')
router.register(r'rolpermission', RolPermissionViewSet, basename='rolpermission')

urlpatterns = router.urls + [ 
    path('rolpermissionfilter/', RolPermissionFilter.as_view(), name='rolpermissionfilter'),
    path('rolfilter/', RolFilter.as_view(), name='rolfilter'), 
    path('userfilter/', UserFilter.as_view(), name='userfilter'),
    ]