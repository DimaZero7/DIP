from django.urls import path

from .views import *

app_name = 'account'
 
urlpatterns = [
    path('', account, name='account'),
    path('editing/', editing, name='editing'),
    path('order_detail/', order_detail, name='order_detail'),
    path('switch', switch, name='switch'),
]