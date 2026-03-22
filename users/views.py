from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from core.permissions.default import GlobalDefaulPermission

from .models import User
from .serializers import UserSerializer

class UserLisCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated, GlobalDefaulPermission]
    queryset = User.objects.all()
    serializer_class = UserSerializer