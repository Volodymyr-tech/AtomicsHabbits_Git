from django.urls import include, path
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

from users.views import RegisterView, UserProfileViewSet

router = DefaultRouter()
router.register(r"profiles", UserProfileViewSet)
# router.register(r'subscriptions', SubscriptionViewSet)

app_name = "users"

urlpatterns = [
    path("", include(router.urls)),  # Include the generated API endpoints
    path("register/", RegisterView.as_view(), name="register"),
    path(
        "login/",
        TokenObtainPairView.as_view(permission_classes=(AllowAny,)),
        name="token_obtain_pair",
    ),
    path("token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
