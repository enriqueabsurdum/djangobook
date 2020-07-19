"""Books URLs"""

# Django
from django.urls import include, path

# Views
from .views import (
    hello_world,
    current_view_url,
    current_view_host,
    current_view_is_secure,
    show_browser,
    show_ip,
    search_form,
    search,
    contact
)

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('current_view_url/', current_view_url, name='current_view_url'),
    path('current_view_host/', current_view_host, name='current_view_host'),
    path('current_view_is_secure/', current_view_is_secure, name='current_view_is_secure'),
    path('show_browser/', show_browser, name='show_browser'),
    path('show_ip/', show_ip, name='show_ip'),
    path('search_form/', search_form, name='search_form'),
    path('search/', search, name='search'),
    path('contact/', contact, name='contact'),
]
