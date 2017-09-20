from django.conf.urls import url

from . views import entry

urlpatterns = [
    url(r'^$', entry),
]
