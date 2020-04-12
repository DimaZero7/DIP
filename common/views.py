from django.views.generic import ListView

from products.models import Product
from poster.models import Poster


class Index(ListView):
    model = Product
    template_name = 'common/index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posters'] = Poster.objects.all()
        return context

 