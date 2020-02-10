from django.conf.urls import url, include
from . import views

app_name = 'ads'

# sarmayedari.ir/

urlpatterns = [
    url(r'^ad/(?P<adID>[0-9]+)$', views.show_ad, name='show_ad'),
    url(r'^premium/(?P<adID>[0-9]+)$', views.show_ad_premium, name='show_ad_premium'),
    url(r'^cat/(?P<catUrl>.+)$', views.show_cat, name='show_cat'),
    url(r'^all$', views.show_all_ads, name='show_all_ads'),
]
