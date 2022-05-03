from django.conf.urls import url,include
from rest_framework import routers
from usermanager.views import *
from django.urls import path, include



urlpatterns = [
    url(r'^', include('rest_auth.urls')),
    url(r'^register_api/$', RegisterAPI.as_view(), name='register'),
    url(r'^login_api/$', LoginAPI.as_view(), name='login'),
    url(r'^user_api/$', UserAPI.as_view(), name='user'),
]