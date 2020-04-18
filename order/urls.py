from django.urls import path

from .views import *

app_name = 'order'

urlpatterns = [
    path('', order_add, name='order_add'),
]
 