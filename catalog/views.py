from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin


from .models import Category, Product, Manufacture
from comments.forms import CommentForm


class CategoriesList(ListView):
    """Список категорий"""
    model = Category
    context_object_name = 'categories'
    template_name = 'catalog/categories_list.html'


class ManufactureList(ListView):
    model = Manufacture
    template_name = 'catalog/manufacture_list.html'
    
    
class CategoryDetail(DetailView, MultipleObjectMixin):
    """Карточка категории со списком товаров"""

    model = Category
    template_name = 'catalog/category_detail.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):

        object_list = Product.objects.filter(categories__slug=self.kwargs.get('slug'))

        if self.request.GET.get('manufacture'):
            object_list = object_list.filter(manufacture__name__in=self.request.GET.getlist('manufacture'))

        if self.request.GET.get('prise_min'):
            object_list = object_list.filter(price__gte=self.request.GET.get('prise_min'))

        if self.request.GET.get('prise_min'):
            object_list = object_list.filter(price__lte=self.request.GET.get('prise_max'))

        if self.request.GET.get('warranty'):
            object_list = object_list.filter(warranty__gte=self.request.GET.get('warranty'))

        if self.request.GET.get('sorting'):
            object_list = object_list.order_by('%s' % (self.request.GET.get('sorting')))

        context = super(CategoryDetail, self).get_context_data(object_list=object_list, **kwargs)
        return context


class ProductDetail(DetailView):
    """Карточка товара"""

    model = Product
    template_name = 'catalog/products_detail.html'

    def get_context_data(self, **kwargs):
        """Добовляю предстовление о форме ввода комментария"""

        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context





