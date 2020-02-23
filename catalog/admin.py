from django.contrib import admin
from .models import *


class ProductsImagesInLine(admin.TabularInline):  # Модель картинок в админке
    model = ProductsImage


class ProductsAdmin(admin.ModelAdmin):  # Добовление в модель товаров модель с картинками в админке
    prepopulated_fields = {"slug": ("name",)}  # Транслирует текст написаный в имя в слуг
    inlines = [
        ProductsImagesInLine,
    ]


admin.site.register(Category)  # Добовляю в админку модель с категориями товаров
admin.site.register(Product, ProductsAdmin)  # Добовляю в админку модель с товарами
