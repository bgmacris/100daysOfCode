from django.urls import path
from django.urls.resolvers import URLPattern
from rest_framework.authtoken import views
from .views import Login, Logout
from .api import test

urlpatterns = [
	path('api_test/', test.as_view(), name="API Test"),
]
