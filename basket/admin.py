from django.contrib import admin
from .models import Status
from .models import Order
from .models import ProductsInOrder
from .models import ProductsInBasket

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass

class ProductsInOrder(admin.TabularInline):
    model = ProductsInOrder
    extra = 0
    can_delete = False
    max_num = 0
    readonly_fields = ('order', 'product', 'price_per_item', 'quantity_nbr', 'total_price', 'created')
    
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_price', 'status', 'created')
    readonly_fields = ('user','total_price', 'created')
    inlines = [
        ProductsInOrder,
    ]
    
    template = 'account/order_detail.html'

@admin.register(ProductsInBasket)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_per_item', 'quantity_nbr', 'total_price', 'is_active', 'created')

