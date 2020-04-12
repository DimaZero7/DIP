from django.contrib import admin
from .models import Orders

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('product', 'price_per_item', 'quantity_nbr', 'total_price', 'is_active')
