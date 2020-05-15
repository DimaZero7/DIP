from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib import messages

from .forms import UserForm, ProfileForm
from basket.models import Order


@login_required(login_url='/authorization/login/')
def account(request):
    return render(request, 'account/account.html')
    

@login_required(login_url='/authorization/login/')
def order_detail(request):
    context = {
        'orders': Order.objects.filter(user=request.user)
    }

    return render(request, 'account/order_detail.html', context)


@login_required(login_url='/authorization/login/')
def editing(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Профиль был обновлен!')
            return redirect('account:account')
        else:
            messages.error(request, 'Исправьте ошибки')
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }
    return render(request, 'account/editing.html', context)