from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from menu.models import Menu
from menu.serializers import MenuSerializer

# Use viewsets instead of API view because it already come with all the needed logic for CRUD ops
class MenuViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]