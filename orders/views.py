from django.shortcuts import render
from django.http import JsonResponse
 
from products.models import Product
from .models import Status
from .models import ProductsInBasket
from .models import ProductsInOrder
from .models import Order
from django.contrib.auth.models import User
from .forms import UserForBasket
    
def basket_add(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    data = request.POST
    product_id = data.get("product_id")
    quantity_nbr = data.get("quantity_nbr")
     
    is_delete = data.get("is_delete")

    if is_delete == 'true':
        ProductsInBasket.objects.filter(id=product_id).update(is_active=False)
    else:
        new_product, created = ProductsInBasket.objects.get_or_create(session_key=session_key, product_id=product_id, is_active=True, defaults={"quantity_nbr":quantity_nbr }  )
        if not created:
            new_product.quantity_nbr += int(quantity_nbr)
            new_product.save(force_update=True)
        
    products_in_basket = ProductsInBasket.objects.filter(session_key=session_key, is_active=True)
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

def basket(request): 
    session_key = request.session.session_key
    product_in_basket = ProductsInBasket.objects.filter(session_key=session_key, is_active=True, order__isnull=True)
    form = UserForBasket(request.POST or None)
    if request.POST:
        print(request.POST)
        if form.is_valid():
            data = request.POST
            username = data["client_username"]
            first_name = data["client_first_name"]
            last_name = data["client_last_name"]
            email = data["client_email"]
            total_price = data["total_price"]
            user, created = User.objects.get_or_create(username=username, first_name=first_name, last_name=last_name, email=email)
            
            order = Order.objects.create(user=user,  first_name=first_name, last_name=last_name, email=email, status_id = 1, total_price=total_price)                                                                                                        
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
        else:
            print("no")

                    
    return render(request, 'basket.html', locals())