from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.serializers import ProductSerializer, ProductPlatformSerializer, PriceAlertSerializer
from products.models import Product, ProductPlatform, PriceAlert

class ProductListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductPlatformListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductPlatform.objects.all()
    serializer_class = ProductPlatformSerializer

class ProductPlatformRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = ProductPlatform.objects.all()
    serializer_class = ProductPlatformSerializer

class PriceAlertListCreateView(ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PriceAlert.objects.all()
    serializer_class = PriceAlertSerializer

class PriceAlertRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = PriceAlert.objects.all()
    serializer_class = PriceAlertSerializer
