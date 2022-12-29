from django.urls import path

from .views import *

app_name = 'common'

urlpatterns = [
    path('', Index.as_view(), name='index'),
    path('about/', about, name='about'),
    path('feedback/', feedback, name='feedback'),
    path('search/', search, name='search'),
    path('delivery/', about_delivery, name='delivery'),
    path('how_to_order/', how_to_order, name='how_to_order'),
    path('payment_methods/', payment_methods, name='payment_methods'),
]
