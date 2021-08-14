from django.conf.urls import url
from django.conf.urls import include

from apps.reed_manga.views import index

urlpatterns = [
    url(r'^$', index, name="index"),
]
