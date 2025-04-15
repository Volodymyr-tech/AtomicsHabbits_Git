from rest_framework import generics, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticated

from atomicshabbits.models import Habbits
from atomicshabbits.paginators import StandardResultsSetPagination
from atomicshabbits.serializers import HabbitsSerializer
from users.permissions import IsOwner


# Create your views here.
class HabbitsViewSet(viewsets.ModelViewSet):
    """UserviewSet allows only authenticated users and admins to see and make changes in objects.
     Also you can filter objects by username and email"""

    queryset = Habbits.objects.all()
    serializer_class = HabbitsSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = [
        "is_public",
        "action",
    ]
    permission_classes = [IsAuthenticated, IsOwner]
    pagination_class = StandardResultsSetPagination

    def get_permissions(self):
        """DRF requires all permissions to return True, and if at least one returns False, it will be 403"""
        if self.action in ["list", "retrieve"]:
            permission_classes = [
                IsAuthenticated,
                IsOwner,
            ]  # authenticated users can view only their courses
        elif self.action in ["update", "partial_update"]:
            permission_classes = [
                IsAuthenticated,
                IsOwner,
            ]  # only moders and owners can change courses
        elif self.action == "create":
            permission_classes = [IsAuthenticated]  # anyone can create course
        elif self.action == "destroy":
            permission_classes = [
                IsAuthenticated,
                IsOwner,
            ]  # only owners can delete courses
        else:
            # Добавляем значение по умолчанию, если self.action не соответствует ни одному из вышеуказанных вариантов
            permission_classes = [IsAuthenticated]

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        """at the list level, only the general permission is checked — that is,
        that the user is authenticated, and the object ownership check is not actually applied to each item.
        """
        return Habbits.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class PublicHabbitsListAPIView(generics.ListAPIView):
    """Authenticated users can view all public hubbits"""

    queryset = Habbits.objects.all()
    serializer_class = HabbitsSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(is_public=True)
