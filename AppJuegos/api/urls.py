from django.urls import path
from AppJuegos.api.api import user_api_view, rol_api_view, section_api_view, permission_api_view, rol_permission_api_view, user_rol_api_view
from AppJuegos.api.api import user_detail_view, rol_detail_view, rol_permission_detail_view, user_rol_detail_view

from AppJuegos.api.views import LoginAPIView, LogoutAPIView, RefreshAPIView

urlpatterns = [
    path('user/', user_api_view, name='user-api'),
    path('rol/', rol_api_view, name='rol-api'),
    path('section/', section_api_view.as_view(), name='section-api'),
    path('permission/', permission_api_view.as_view(), name='permission-api'),
    path('rolpermission/', rol_permission_api_view, name='rolpermission-api'),
    path('userrol/', user_rol_api_view, name='userrol-api'),
    path('user/<str:pk>/', user_detail_view, name='user-detail'),
    path('rol/<int:pk>/', rol_detail_view, name='rol-detail'),
    path('rolpermission/<int:pk>/', rol_permission_detail_view, name='rolpermission-detail'),
    path('userrol/<int:pk>/', user_rol_detail_view, name='userrol-detail'),

    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('refresh/', RefreshAPIView.as_view(), name='refresh'),

]