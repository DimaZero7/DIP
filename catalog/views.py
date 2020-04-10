from django.views.generic import ListView, DetailView

from .models import Category


class CategoriesList(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'catalog/categories_list.html'


class CategoryDetail(DetailView):
    model = Category
    template_name = 'catalog/category_detail.html'
