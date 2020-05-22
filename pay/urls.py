from django.urls import path

from .views import *

app_name = 'pay'

urlpatterns = [
    path('', pay, name='pay'),
    # path('popoln/', popoln, name='popoln'),
    # path('success/', success, name='success'),
    # path('fail/', fail, name='fail'),

]
 