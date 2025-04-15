from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated

from users.models import CustomUser
from users.serializers import RegisterSerializer, UserProfileSerializer


# Create your views here.
class RegisterView(CreateAPIView):
    """Registerview class, allow enyone to register"""

    queryset = CustomUser.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]  # allow anyone to register


class UserProfileViewSet(viewsets.ModelViewSet):
    """UserviewSet allows only authenticated admins to see and make changes in objects.'''
     '''Also you can filter objects by username and email"""

    queryset = CustomUser.objects.all()
    serializer_class = UserProfileSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "username",
        "email",
    ]
    permission_classes = [IsAuthenticated, IsAdminUser]
