from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

app_name = 'product'

urlpatterns = [
    # Перенаправление в каталог
    path('', RedirectView.as_view(url='/catalog/')),

    path('<str:slug>/', ProductDetail.as_view(), name='detail'),

]
