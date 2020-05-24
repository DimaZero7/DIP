from django.shortcuts import render
from django.urls import reverse
from catalog.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q #Создание сложных запросов к бд

def result(request):
    search = request.GET.get('search')
    
    if not search == '':
        product_search = Product.objects.filter( Q(name__icontains=search) | Q(manufacture__name__icontains=search))
        search = {
            'product_search':product_search
        }

        return render(request, 'result.html', search)
    else:
        messages.error(request, 'Ошибка, поле пустое')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))