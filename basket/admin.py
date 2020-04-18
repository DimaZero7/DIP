from django.contrib import admin
from .models import Status
from .models import Order
from .models import ProductsInOrder
from .models import ProductsInBasket

@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'first_name', 'last_name', 'total_price', 'status', 'created')
    readonly_fields = ('user', 'first_name', 'last_name', 'total_price', 'created')

@admin.register(ProductsInOrder)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'price_per_item', 'quantity_nbr', 'total_price', 'is_active', 'created')

@admin.register(ProductsInBasket)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_per_item', 'quantity_nbr', 'total_price', 'is_active', 'created')
