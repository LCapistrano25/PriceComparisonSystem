from django.urls import path
from products.views import (
    ProductListCreateView, 
    ProductRetrieveUpdateDestroyView,
    ProductPlatformListCreateView,
    ProductPlatformRetrieveUpdateDestroyView,
    PriceAlertListCreateView,
    PriceAlertRetrieveUpdateDestroyView,
    PriceHistoryListCreateView,
    PriceHistoryRetrieveUpdateDestroyView,
)

urlpatterns = [
    path('products/', ProductListCreateView.as_view(), name='product-list-create'),
    path('products/<int:pk>/', ProductRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
    path('products/platforms/', ProductPlatformListCreateView.as_view(), name='product-platform-list-create'),
    path('products/platforms/<int:pk>/', ProductPlatformRetrieveUpdateDestroyView.as_view(), name='product-platform-retrieve-update-destroy'),
    path('products/alerts/', PriceAlertListCreateView.as_view(), name='price-alert-list-create'),
    path('products/alerts/<int:pk>/', PriceAlertRetrieveUpdateDestroyView.as_view(), name='price-alert-retrieve-update-destroy'),
    path('products/history/', PriceHistoryListCreateView.as_view(), name='price-history-list-create'),
    path('products/history/<int:pk>/', PriceHistoryRetrieveUpdateDestroyView.as_view(), name='price-history-retrieve-update-destroy'),
]