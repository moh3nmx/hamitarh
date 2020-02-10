from django.conf.urls import url, include
from . import views
from ads import views as ad_views

app_name = 'my'

# User ads management
urlpatterns = [
    # User Create new Ad
    url(r'^new_ad$', views.create_ad, name='create_ad'),
    # User Create new Ad
    url(r'^edit/(?P<adID>[0-9]+)$', views.edit_ad, name='edit_ad'),
    # Show User Adds
    url(r'^ads$', views.show_all_ads, name='all_ads'),
    # User Control-Panel
    url(r'^panel$', views.panel_page, name='panel'),
    # Delete Ad
    url(r'^delete/(?P<adID>[0-9]+)$', views.delete_ad, name='delete_ad'),
    # Change Password in panel
    url(r'^pass$', views.change_pass, name='pass'),
    # Investment process
    url(r'^(?P<adID>[0-9]+)/invest$', views.investment , name='investment'),
    ]
