from django.urls import path
from .views import UserLisCreateAPIView

urlpatterns = [
    path('users/', UserLisCreateAPIView.as_view(), name='user-list-create'),
]