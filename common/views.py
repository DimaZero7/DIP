from django.shortcuts import render
from catalog.models import Product


def index(request):
    products_posters = Product.objects.filter(slider=True)
    context = {
        'products_posters': products_posters,
    }
    return render(request, 'common/index.html', context)
