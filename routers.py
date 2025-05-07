from rest_framework import routers
from menu.viewsets import MenuViewSet

router = routers.SimpleRouter() #automatically generates urls for DRF Viewset
router.register(r'menu', MenuViewSet, basename='menu')

urlpatterns = router.urls