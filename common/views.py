from django.views.generic import ListView

from catalog.models import Product


class Index(ListView):
    model = Product
    template_name = 'common/index.html'
