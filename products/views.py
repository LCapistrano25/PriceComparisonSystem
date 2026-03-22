from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from products.serializers import ProductSerializer, ProductPlatformSerializer
from products.models import Product, ProductPlatform

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
