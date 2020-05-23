# views.py

from django.shortcuts import get_object_or_404, render
from django.contrib.auth.decorators import login_required
from basket.models import Order
from robokassa.forms import RobokassaForm
from robokassa.signals import result_received


@login_required(login_url='/authorization/login/')
def pay(request):

    order = Order.objects.get(user=request.user, status_id = 1)

    form = RobokassaForm(initial={
               'OutSum': order.total_price,
               'InvId': order.id,
               'Email': request.user.email,
           })

    context = {
        'orders': Order.objects.filter(user=request.user, status_id = 1),
        'form':form
    }
    
    return render(request, 'pay/pay.html', context)


def payment_received(sender, **kwargs):
    order = Order.objects.get(id=kwargs['InvId']) #Получаем оплаченный заказ
    order.status_id  = 2  # меняем статус заказа
    order.total_price = kwargs['OutSum'] # сравниваем сумму заказа и сумму оплаты
    order.save()

result_received.connect(payment_received)

