from django.views.generic import DetailView

from .models import Product
from comments.forms import CommentForm

def product(request, product_id):
    product = Product.objects.get(id=product_id)

    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()

    print(request.session.session_key)


class ProductDetail(DetailView):
    """Карточка товара"""
    
    model = Product
    template_name = 'products/products_detail.html'
    
    def get_context_data(self, **kwargs):
        """Добовляю предстовление о форме ввода комментария"""

        context = super().get_context_data(**kwargs)
        context['comment_form'] = CommentForm()
        return context