from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path(
        'manage/',
        admin.site.urls
    ),
    path(
        'accounts/',
        include('Core.urls')
    ),
    path(
        '',
        include('dashboard.urls')
    ),
    path(
        'content/',
        include('content.urls')
    ),

    # api url includes...................
    path(
        '',
        include('Core.api.urls')
    ),
    path(
        'member/',
        include('member.api.urls')
    ),
]

# Add this at the end of the file to serve static files in development
if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL,
        document_root=settings.STATIC_ROOT
    )
