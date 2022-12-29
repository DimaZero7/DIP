from django.http import JsonResponse
from django.shortcuts import render, redirect, HttpResponse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .forms import UserForBasket
from .models import *
from catalog.models import Product
from django.db.models import F #Для того что бы производить арифметику с полями бд

def basket_add(request):
    return_dict = dict()

    data = request.POST
    product_id = data.get("product_id")
    quantity_nbr = data.get("quantity_nbr")
    is_delete = data.get("is_delete")
        
    if is_delete == 'true':
        ProductsInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductsInBasket.objects.get_or_create(user=request.user, product_id=product_id, is_active=True, defaults={"quantity_nbr":quantity_nbr }  )
        if not created:
            new_product.quantity_nbr += int(quantity_nbr)
            new_product.save(force_update=True)


    products_in_basket = ProductsInBasket.objects.filter(user=request.user, is_active=True)
    product_total_quantity_nbr = products_in_basket.count()  
    return_dict["product_total_quantity_nbr"] = product_total_quantity_nbr

    return_dict["products"] = list()
    for item in products_in_basket:
        product_dict = dict()
        product_dict["id"] = item.id
        product_dict["name"] = item.product.name
        product_dict["price_per_item"] = item.price_per_item
        product_dict["quantity_nbr"] = item.quantity_nbr
        return_dict["products"].append(product_dict)
    return JsonResponse(return_dict)



#Создание заказов
@login_required(login_url='/auth/login/')
def order_add(request):

    product_in_basket = ProductsInBasket.objects.filter(user=request.user, is_active=True, order__isnull=True)
    form = UserForBasket(request.POST or None)
    if request.POST:
        if form.is_valid():
            data = request.POST
            username = data["client_username"]
            total_price = data["total_price"]
            comment = data["comment"]
            user = User.objects.get(username=username)
             
            order = Order.objects.create(user=user, status_id = 1, total_price=total_price, comment=comment)
            print(order)
            
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductsInBasket.objects.get(id=product_in_basket_id)
                    
                    product_in_basket.quantity_nbr = value
                    product_in_basket.order = order
                    product_in_basket.is_active = False
                    
                    #Изменяем количество товара на складе при заказе 
                    product_in_basket.product.warehouse -= int(product_in_basket.quantity_nbr)
                    product_in_basket.product.save()
                    product_in_basket.save(force_update=True)
                    
                    ProductsInOrder.objects.create(product=product_in_basket.product,
                                                   quantity_nbr = product_in_basket.quantity_nbr, 
                                                   price_per_item = product_in_basket.price_per_item, 
                                                   total_price=product_in_basket.total_price, 
                                                   order = order)
            messages.error(request, 'Заказ создан')
            return redirect('account:order_detail')
        else:
            print("no")

                    
    return render(request, 'basket/basket.html', locals())



@login_required(login_url='/authorization/login/')
def pay(request):
    order = Order.objects.filter(user=request.user, status=1)
    context = {
        "order":order,
    }
    return render(request, 'basket/pay.html', context)

@login_required(login_url='/authorization/login/')

def pay_success(request):
    Order.objects.filter(user=request.user, status=1).update(status_id=2)
    messages.success(request, 'Заказ Оплачен')
    return redirect('account:order_detail')


def interaction_order(request):
    data = request.POST
    print(data)
    order_status = data.get("order_status")
    order_id = data.get("order_id")
    
    if order_status == 'pay':
        Order.objects.filter(user=request.user, status=1, id=order_id).update(status_id=2)
        
    if order_status == 'completion':
        Order.objects.filter(user=request.user, status=2, id=order_id).update(status_id=3)
    
    return HttpResponse()
