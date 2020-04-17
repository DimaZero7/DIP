from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin

from .models import Category
from products.models import Product


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
