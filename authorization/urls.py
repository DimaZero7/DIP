from django.urls import path

from .views import *

app_name = 'authorization'

urlpatterns = [
    # /
    path('', login, name='login'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
]
