from django.urls import path

from AppJuegos.api.views import LoginAPIView, LogoutAPIView, RefreshAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),
    path('refresh/', RefreshAPIView.as_view(), name='refresh'),
]