from django.shortcuts import render
from django.http import JsonResponse
from .models import ProductsInBasket
 
#Добавление товаров в корзину
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