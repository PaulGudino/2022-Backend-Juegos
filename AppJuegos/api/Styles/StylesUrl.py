from rest_framework.routers import DefaultRouter
from AppJuegos.api.Styles.StylesApiViews import (
    StylesViewSet,
)

router = DefaultRouter()
router.register(r'design', StylesViewSet, basename='Design')

urlpatterns = router.urls