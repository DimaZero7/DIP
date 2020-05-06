from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import Category
from products.models import Product

from django.shortcuts import render
from django.http import JsonResponse


class CategoriesList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'catalog/categories_list.html'


class CategoryDetail(DetailView, MultipleObjectMixin):
    model = Category
    template_name = 'catalog/category_detail.html'
    paginate_by = 1

    def get_context_data(self, **kwargs):
        object_list = Product.objects.filter(categories__slug=self.kwargs.get('slug'))
        context = super(CategoryDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context

    

#Фильтрация товаров
def filter(request):
    data = request.POST
    filter = data.get("filter")
    
    print(filter)
    if filter == 'nameAZ':
        filters = Product.objects.all().order_by('name')
        context = {
            'filters':filters
        }
    
    if filter == 'nameZA':
        filters = Product.objects.all().order_by('-name')
        context = {
            'filters':filters
        }
    
    if filter == 'priceIncrement':
        filters = Product.objects.all().order_by('price')
        context = {
            'filters':filters
        }
    if filter == 'priceDeincrement':
        filters = Product.objects.all().order_by('-price')
        context = {
            'filters':filters
        }
    
    if filter == 'dataIncrement':
        filters = Product.objects.all().order_by('date')
        context = {
            'filters':filters
        }
    if filter == 'dataDeincrement':
        filters = Product.objects.all().order_by('-date')
        context = {
            'filters':filters
        }
    return render(request, 'catalog/result_filter.html', context)

