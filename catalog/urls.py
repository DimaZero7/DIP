from django.urls import path
from .views import *

urlpatterns = [
        path('category/', category_list, name='category_list_url'),
        path('category/<str:slug>/', CategoryDetail.as_view(), name='category_detail_url'),  # Карточка каталог
        path('product/<str:slug>/', ProductDetail.as_view(), name='product_detail_url'),  # Карточка товара

        # **********************************
        path('product/<slug:slug>/add_comment/', CommentDetail.as_view(), name = 'add_comment'), 
]
