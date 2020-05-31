from django.views.generic import ListView

from catalog.models import Product


class Index(ListView):
    model = Product
    template_name = 'common/index.html'

#def about(request):
#
#    return render(request, 'common/about.html')