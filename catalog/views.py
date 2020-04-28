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

    



##Фильтрация товаров
#def filter(request):
#    filter = request.GET.get('filter')
#    
#    print(filter)
##    if filter == 'price_descending':
##        product_filter = Product.objects.all().order_by('-price')
##    
##    if filter == 'price_ascending':
##        product_filter = Product.objects.all().order_by('price')
##    
##    context = {
##        'product_filter':product_filter
##    }
##
##    return render(request, 'result_filter.html', context)
