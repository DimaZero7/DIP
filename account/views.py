from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from basket.models import Order
from .forms import UserForm, ProfileForm
from django.shortcuts import  redirect
from django.contrib import messages

@login_required(login_url='/auth/login/')
def account(request):
    user_form = UserForm(instance=request.user)
    profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'account.html',{
        'user_form': user_form,
        'profile_form': profile_form
    })
    

@login_required(login_url='/auth/login/')
def order_detail(request):
    context = {
        'orders': Order.objects.filter(user=request.user)
    }

    return render(request, 'order_detail.html', context)


@login_required(login_url='/auth/login/')
def editing(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Ваш профиль был успешно обновлен!'))
            return redirect('account:account')
        else:
            messages.error(request, ('Пожалуйста, исправьте ошибки.'))
            pass
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'editing.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })