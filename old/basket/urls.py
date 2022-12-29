from django.urls import path

from .views import *

app_name = 'basket'

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('order_add/', order_add, name='order_add'),
    path('interaction_order/', interaction_order, name='interaction_order'),
]
