from django.views.generic import ListView
from django.shortcuts import render, redirect
from django.urls import reverse
from catalog.models import Product
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q #Создание сложных запросов к бд

from .models import Feedback

class Index(ListView):
    model = Product
    template_name = 'common/index.html'
    ordering = ['-date']
    
def about(request):
    return render(request, 'common/about.html')


def feedback(request):
    return render(request, 'common/feedback.html')


def feedback(request):
    if request.POST:
        data = request.POST
        user = data.get("user")
        email = data.get("email")
        message = data.get("message")
        feedback = Feedback.objects.create(user=user, email = email, message=message)
        feedback.save()
        
        messages.success(request, 'Сообщение отправлено')
        return redirect(reverse('common:index'))

    return render(request, 'common/feedback.html')


def about_delivery(request):
    return render(request, 'common/delivery.html')


def how_to_order(request):
    return render(request, 'common/how_to_order.html')


def payment_methods(request):
    return render(request, 'common/payment_methods.html')


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