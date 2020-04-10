from django.urls import path

from .views import *

app_name = 'manufacture'

urlpatterns = [
    path('', ManufactureList.as_view(), name='list'),
    path('<str:slug>/', ManufactureDetail.as_view(), name='detail'),
]
