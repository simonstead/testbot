from django.conf.urls import include, url
from .views import fb_testbot
urlpatterns = [
    url(r'^54d90dab9152e50f2ae5cc06050cd55c68a1bb4921e6d1b290/?$', fb_testbot.as_view())
]
