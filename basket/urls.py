from django.urls import path

from .views import *

app_name = 'basket'

urlpatterns = [
    path('', basket, name='basket'),
]
 