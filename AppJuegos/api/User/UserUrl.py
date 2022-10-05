from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.User.UserApiviews import (
    UserCreateViewSet,
    UserViewSet,
    UserFilter
)



router = DefaultRouter()
router.register(r'create/user', UserCreateViewSet, basename='createuser')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls + [ 
    path('userfilter/', UserFilter.as_view(), name='userfilter'),
]


