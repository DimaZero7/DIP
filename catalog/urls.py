from django.urls import path
from django.views.generic.base import RedirectView

from .views import *

app_name = 'catalog'

urlpatterns = [
    path('', CategoriesList.as_view(), name='categories_list'),
    path('<str:slug>/', CategoryDetail.as_view(), name='category_detail'),
    path('product/', RedirectView.as_view(url='/catalog/')),
    path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail'),
]
