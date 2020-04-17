from django.urls import path

from .views import *

app_name = 'orders'

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('basket/', basket, name='basket'), 
]
 