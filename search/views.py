from django.shortcuts import render
from django.urls import reverse
from products.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
    
def result(request):
    search = request.GET.get('search')
    
    if not search == '':
        product_search = Product.objects.filter(name__icontains=search)
        context = {
            'product_search':product_search
        }

        return render(request, 'result.html', context)
    else:
        messages.error(request, 'Ошибка, поле пустое')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))