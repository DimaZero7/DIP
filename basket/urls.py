from django.urls import path

from .views import *

app_name = 'basket'

urlpatterns = [
    path('basket_add/', basket_add, name='basket_add'),
    path('order_add/', order_add, name='order_add'),
    path('pay/', pay, name='pay'),
    path('pay_success/', pay_success, name='pay_success'),
]
