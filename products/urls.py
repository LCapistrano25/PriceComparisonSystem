from django.urls import path
from products.views import (
    ProductListCreateView, 
    ProductRetrieveUpdateDestroyView,
    ProductPlatformListCreateView,
    ProductPlatformRetrieveUpdateDestroyView
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    path('products/platforms/', ProductPlatformListCreateView.as_view(), name='product-platform-list-create'),
    path('products/platforms/<int:pk>/', ProductPlatformRetrieveUpdateDestroyView.as_view(), name='product-platform-retrieve-update-destroy'),
    
]