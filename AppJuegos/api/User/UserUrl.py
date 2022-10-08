from rest_framework.routers import DefaultRouter
from django.urls import path
from AppJuegos.api.User.UserApiviews import (
    UserCreateViewSet,
    UserViewSet,
    UserFilterRol,
    UserFilterIsEliminated
)



router = DefaultRouter()
router.register(r'create/user', UserCreateViewSet, basename='createuser')
router.register(r'user', UserViewSet, basename='user')

urlpatterns = router.urls + [ 
    path('userfilterrol/', UserFilterRol.as_view(), name='userfilter'),
    path('userfilteriseliminated/', UserFilterIsEliminated.as_view(), name='userfilteriseliminated'),
]


