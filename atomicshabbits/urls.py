from django.urls import include, path
from rest_framework.routers import DefaultRouter

from atomicshabbits.views import HabbitsViewSet, PublicHabbitsListAPIView

router = DefaultRouter()
router.register(r"habbits", HabbitsViewSet)


app_name = "atomicshabbits"

urlpatterns = [
    path("", include(router.urls)),  # Include the generated API endpoints
    path(
        "public-habbits/",
        PublicHabbitsListAPIView.as_view(),
        name="public_habbits",
    ),
]
