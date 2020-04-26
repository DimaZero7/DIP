from django.shortcuts import render
from products.models import Product


    
def result(request):
    search = request.GET.get('search')
    product_search = Product.objects.filter(name__icontains=search)
    context = {
        'product_search':product_search
    }

    return render(request, 'result.html', context)
