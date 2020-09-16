from django.conf import settings
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView
from django.views import defaults as default_views
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.documentation import include_docs_urls

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Nzembo API",
        default_version='v1',
        description="Nzembo is a platform that allows people to share lyrics, translations of CD songs",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(
            email="espoir.mur@gmail.com", name="Espoir Murhabazi", url="https://murhabazi.com/"
        ),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path("", TemplateView.as_view(template_name="pages/home.html"), name="home"),
    re_path(r'^app/(?P<route>.*)$', TemplateView.as_view(template_name="index.html"), name='app'),
    path("about/", TemplateView.as_view(template_name="pages/about.html"), name="about"),
    path("users/", include("backend.users.urls", namespace="users")),
    path("accounts/", include("allauth.urls")),
    path(settings.ADMIN_URL, admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path("api/", include("config.api_router")),
    path("auth-token/", obtain_auth_token),
    path("api-docs/", include_docs_urls(title="backend REST API", public=False)),
]

if settings.DEBUG:
    # This allows the error pages to be debugged during development, just visit
    # these url in browser to see how these error pages look like.
    urlpatterns += [
        path(
            "400/",
            default_views.bad_request,
            kwargs={"exception": Exception("Bad Request!")},
        ),
        path(
            "403/",
            default_views.permission_denied,
            kwargs={"exception": Exception("Permission Denied")},
        ),
        path(
            "404/",
            default_views.page_not_found,
            kwargs={"exception": Exception("Page not Found")},
        ),
        path("500/", default_views.server_error),
    ]
    if "debug_toolbar" in settings.INSTALLED_APPS:
        import debug_toolbar

        urlpatterns = [path("__debug__/", include(debug_toolbar.urls))] + urlpatterns
