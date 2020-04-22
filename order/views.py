from django.shortcuts import render
from products.models import Product
from basket.models import Status
from basket.models import ProductsInBasket
from basket.models import ProductsInOrder
from basket.models import Order
from django.contrib.auth.models import User
from .forms import UserForBasket
from django.contrib.auth.decorators import login_required

#Создание заказов
@login_required(login_url='/auth/login/')
def order_add(request):
    session_key = request.session.session_key
    product_in_basket = ProductsInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = UserForBasket(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            username = data["client_username"]
            total_price = data["total_price"]
            user = User.objects.get(username=username)
             
            order = Order.objects.create(user=user, status_id = 1, total_price=total_price)                                                                                                        
            for name, value in data.items():
                if name.startswith("product_in_basket_"):
                    product_in_basket_id = name.split("product_in_basket_")[1]
                    product_in_basket = ProductsInBasket.objects.get(id=product_in_basket_id)
                    
                    product_in_basket.quantity_nbr = value
                    product_in_basket.order = order
                    product_in_basket.save(force_update=True)
                    
                    ProductsInOrder.objects.create(product=product_in_basket.product,
                                                   quantity_nbr = product_in_basket.quantity_nbr, 
                                                   price_per_item = product_in_basket.price_per_item, 
                                                   total_price=product_in_basket.total_price, 
                                                   order = order)
#                    ProductsInBasket.objects.update(is_active=False)
        else:
            print("no")

                    
    return render(request, 'basket.html', locals())