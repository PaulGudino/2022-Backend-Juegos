from django.urls import path

from AppJuegos.api.api import (
    User_ListCreate_APIView,
    User_RetrieveUpdateDestroy_APIView,
    Rol_ListCreate_APIView,
    Rol_RetrieveUpdateDestroy_APIView,
    Permission_List_APIView,
    RolPermission_ListCreate_APIView,
    RolPermission_RetrieveUpdateDestroy_APIView
)

from AppJuegos.api.views import LoginAPIView, LogoutAPIView, RefreshAPIView

urlpatterns = [
    path('user/', User_ListCreate_APIView.as_view(), name='user-list'),
    path('user/<int:pk>/', User_RetrieveUpdateDestroy_APIView.as_view(), name='user-detail'),
    path('rol/', Rol_ListCreate_APIView.as_view(), name='rol-list'),
    path('rol/<int:pk>/', Rol_RetrieveUpdateDestroy_APIView.as_view(), name='rol-detail'),
    path('permission/', Permission_List_APIView.as_view(), name='permission-list'),
    path('rolpermission/', RolPermission_ListCreate_APIView.as_view(), name='rolpermission-list'),
    path('rolpermission/<int:pk>/', RolPermission_RetrieveUpdateDestroy_APIView.as_view(), name='rolpermission-detail'),

    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('refresh/', RefreshAPIView.as_view(), name='refresh'),

]