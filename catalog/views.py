from django.views.generic import ListView, DetailView
from django.views.generic.list import MultipleObjectMixin
from django.db.models import Q


from .models import Category, Product
from comments.forms import CommentForm


class CategoriesList(ListView):
    """Список категорий"""
    model = Category
    context_object_name = 'categories'
    template_name = 'catalog/categories_list.html'


class CategoryDetail(DetailView, MultipleObjectMixin):
    """Карточка категории со списком товаров"""

    model = Category
    template_name = 'catalog/category_detail.html'
    paginate_by = 4

    def get_context_data(self, **kwargs):

        object_list = Product.objects.filter(categories__slug=self.kwargs.get('slug'))

        if self.request.GET.get('manufacture'):
            object_list = object_list.filter(
                Q(manufacture__name=self.request.GET.get('manufacture'))
            )

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





