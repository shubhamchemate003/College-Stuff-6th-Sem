from django.conf.urls import url, include
from rest_framework import routers
from django.conf.urls import url, re_path
from .views import *

urlpatterns = [
    url(r'^add_items/$', AddItems.as_view(), name='get_items'),
    url(r'^get_items/$', GetItems.as_view(), name='get_items'),
    url(r'^place_order/$', PlaceOrder.as_view(), name='place_order'),
    url(r'^get_customer_orders/$', GetCustomerOrders.as_view(), name='get_customer_orders'),
    url(r'^get_dp_orders/$', GetDPOrders.as_view(), name='get_dp_orders'),
]