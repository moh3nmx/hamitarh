from django.conf.urls import url, include
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static
import debug_toolbar

import ckeditor_uploader

urlpatterns = [
    # admin
    url(r'^admin/', admin.site.urls),

    # url("^$", direct_to_template, {"template": "index.html"}, name="home"),
    url(r'^', include('mainapp.urls')),

    # Authentication
    url(r'^', include('authentication.urls')),

    # Advertisements
    url(r'^', include('ads.urls')),

    # My Panel
    url(r'^my/', include('my.urls')),


]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]