from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.models import Order

@login_required(login_url='/auth/login/')
def account(request):
    
    return render(request, 'account.html')

@login_required(login_url='/auth/login/')
def order_detail(request):
    context = {
        'orders': Order.objects.filter(user=request.user)
    }

    return render(request, 'order_detail.html', context)


@login_required(login_url='/auth/login/')
def editing(request):
    
    return render(request, 'editing.html')
