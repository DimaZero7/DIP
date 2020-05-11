from .models import ProductsInBasket


def get_basket_item(request):
    if request.user.is_anonymous:
        products_in_basket = ProductsInBasket.objects.filter(user=request.user.is_anonymous, is_active=True, order__isnull=True)
        product_total_quantity_nbr = products_in_basket.count()  
        return locals()
    else:
        products_in_basket = ProductsInBasket.objects.filter(user=request.user, is_active=True, order__isnull=True)
        product_total_quantity_nbr = products_in_basket.count()  
        return locals()
