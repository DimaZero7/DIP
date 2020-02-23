from django.views.generic import View
from django.shortcuts import render
from .models import Category, Product
from .utils import ObjectDetailMixin


def category_list(request):
    context = {

    }
    return render(request, 'catalog/categorys/category_list.html', context)


class CategoryDetail(ObjectDetailMixin, View):
    model = Category
    template = 'catalog/categorys/category_detail.html'


class ProductDetail(ObjectDetailMixin, View):
    model = Product
    template = 'catalog/categorys/products/products_detail.html'
