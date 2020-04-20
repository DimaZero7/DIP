from django.urls import path
from django.conf.urls import include, url
from .views import *

app_name = 'account'

urlpatterns = [
    path('order_detail/', order_detail, name='order_detail'),
    path('', account, name='account'),
]

