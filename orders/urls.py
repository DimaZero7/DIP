from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('', basket_add, name='basket_add'),
]
