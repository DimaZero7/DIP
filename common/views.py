from django.views.generic import ListView
from django.shortcuts import render
from catalog.models import Product
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q #Создание сложных запросов к бд

class Index(ListView):
    model = Product
    template_name = 'common/index.html'

def about(request):

    return render(request, 'common/about.html')

def feedback(request):

    return render(request, 'common/feedback.html')


def search(request):
    search = request.GET.get('search')
    
    if not search == '':
        product_search = Product.objects.filter( Q(name__icontains=search) | Q(manufacture__name__icontains=search))
        search = {
            'product_search':product_search
        }

        return render(request, 'common/search.html', search)
    else:
        messages.error(request, 'Ошибка, поле пустое')
        return HttpResponseRedirect(request.META.get('HTTP_REFERER','/'))