from django.urls import path
from django.conf.urls import include, url
from .views import *

app_name = 'account'

urlpatterns = [
    path('', account, name='account'),
]

