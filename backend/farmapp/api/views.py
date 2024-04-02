from rest_framework.viewsets import ModelViewSet
from ..models import Farm, Product
from .serializers import FarmSerializer, ProductSerializer


class FarmViewSet(ModelViewSet):
    """
    A viewset for viewing and editing farm instances.
    """
    queryset = Farm.objects.all()
    serializer_class = FarmSerializer

class ProductViewSet(ModelViewSet):
    """
    A viewset for viewing and editing product instances.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer