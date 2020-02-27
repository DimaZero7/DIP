from django.shortcuts import render
from django.views.generic import View
from catalog.utils import ObjectDetailMixin
from catalog.models import Product, Manufacture


def index(request):
    products = Product.objects.all()
    products_posters = Product.objects.filter(slider=True)
    context = {
        'products_posters': products_posters,
        'products': products,
    }
    return render(request, 'common/index.html', context)



def manufacturers_list(request):
    list_manufacturers = Manufacture.objects.all()
    context = {
        'list_manufacturers': list_manufacturers,
    }
    return render(request, 'common/manufacturers/manufacturers_list.html', context)


class ManufacturersDetail(ObjectDetailMixin, View):
    model = Manufacture
    template = 'common/manufacturers/manufacturers_detail.html'
