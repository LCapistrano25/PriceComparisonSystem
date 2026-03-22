from django.urls import path
from .views import UserLisCreateAPIView, UserRetrieveUpdateDestroyAPIView

urlpatterns = [
    path('users/', UserLisCreateAPIView.as_view(), name='user-list-create'),
    path('users/<int:pk>/', UserRetrieveUpdateDestroyAPIView.as_view(), name='user-retrieve-update-destroy'),
]