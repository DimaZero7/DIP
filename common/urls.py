from django.urls import path

from .views import *

app_name = 'common'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('search/', search, name='search'),
]
