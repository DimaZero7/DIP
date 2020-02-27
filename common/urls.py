from django.urls import path
from .views import *


urlpatterns = [
    path('', index, name='index_url'),  # Главная
    path('manufacturers/', manufacturers_list, name='manufacturers_list_url'),  # Список производителей
    path('manufacturers/<str:slug>', ManufacturersDetail.as_view(), name='manufacturers_detail_url')
]