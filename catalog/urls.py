from django.urls import path

from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('<str:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('filter', filter, name='filter'),
]
