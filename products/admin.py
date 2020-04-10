from django.contrib import admin

from .models import Product, ProductsImage
from poster.admin import PosterInLine


class ProductsImagesInLine(admin.TabularInline):
    """Предстовление о картинках товаров"""

    model = ProductsImage


class ProductsAdmin(admin.ModelAdmin):
    """Предстовление товаров"""

    inlines = [
        ProductsImagesInLine,
        PosterInLine,
    ]

    prepopulated_fields = {"slug": ("name",)}

    list_display = ('name', 'warehouse', 'price')

    fieldsets = [
        ('Общее', {'fields': ['categories', 'manufacture']}),
        ('Наименование товара', {'fields': ['name', 'slug']}),
        ('Основное', {'fields': ['price', 'warehouse', 'warranty']}),
        ('Описание', {'fields': ['description', 'specifications', 'set']}),
    ]


admin.site.register(Product, ProductsAdmin)
