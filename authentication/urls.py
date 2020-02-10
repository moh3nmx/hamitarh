from django.conf.urls import url, include
from . import views
from ads import views as ad_views

app_name = 'authentication'

# sarmayedari.ir/

# User info pages
urlpatterns = [
    # Register to Site
    url(r'^register$', views.register_page, name='register'),
    # Login to Site
    url(r'^login$', views.login_page, name='login'),
    # Logout from Site
    url(r'^logout$', views.logout_page, name='logout'),
    # Subscribe
    url(r'^sub$', views.subscription, name='sub'),
    ]

