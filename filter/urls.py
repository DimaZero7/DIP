from django.urls import path

from .views import *

app_name = 'filter'

urlpatterns = [
    path('', filter, name='filter'),
]
