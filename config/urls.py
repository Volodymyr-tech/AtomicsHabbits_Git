from django.contrib import admin
from django.urls import include, path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation for tracking application AtomicsHabbits",
        default_version="v1",
        description="This API is designed to create and manage user habits. It allows you to register,"
        " log in, add useful and pleasant habits, link them together, and receive reminders via Telegram."
        " The user can track the fulfillment of habits, specify rewards, and share public habits with others."
        " The API supports JWT authentication, business logic validation, and pagination.",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "docs/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path(
        "redoc/",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
    path("api/", include("atomicshabbits.urls", namespace="atomicshabbits")),
    path("api/users/", include("users.urls")),
]
