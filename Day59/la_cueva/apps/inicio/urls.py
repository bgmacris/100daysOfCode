from django.conf.urls import url
from django.conf.urls import include

from apps.inicio.views import index

urlpatterns = [
    url(r'^$', index),
]
