from django.urls import path
from AppJuegos.api.views import Login, Logout, ForgotPasswordView, ResetForgotPasswordView

urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-forgot-password/', ResetForgotPasswordView.as_view(), name='reset-forgot-password'),
]