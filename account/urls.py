from django.urls import path

from .views import *

app_name = 'account'

urlpatterns = [
    path('', account, name='account'),
    path('order_detail/', order_detail, name='order_detail'),
    path('editing/', editing, name='editing'),
]

