from django.views.generic import DetailView

from .models import Product
from comments.forms import CommentForm


class ProductDetail(DetailView):
    """Карточка товара"""

    model = Product
    template_name = 'products/products_detail.html'

    def get_context_data(self, **kwargs):
        """Добовляю предстовление о форме ввода ком ентария"""

        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm('product')
        return context

