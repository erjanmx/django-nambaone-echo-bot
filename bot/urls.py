from django.conf.urls import url

from bot.views import entry

urlpatterns = [
    url(r'^$', entry),
]
