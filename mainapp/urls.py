from django.conf.urls import url, include
from django.contrib.sitemaps.views import sitemap

from .sitemaps import StaticViewSitemap
from . import views


sitemaps = {
    'static': StaticViewSitemap,
}


app_name = 'mainapp'

urlpatterns = [
    # index of site
    url(r'^$', views.index, name='index'),
    # ck Editor
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

]
