from .models import ProductsInBasket

def get_basket_item(request):
    session_key = request.session.session_key
    if not session_key:
        request.session.cycle_key()
    products_in_basket = ProductsInBasket.objects.filter(session_key=session_key, is_active=True)
    product_total_quantity_nbr = products_in_basket.count()  
    return locals()