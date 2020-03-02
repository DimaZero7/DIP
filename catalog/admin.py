from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ProductsImagesInLine(admin.TabularInline):  # Модель картинок в админке
    model = ProductsImage


@admin.register(Product)
class ProductsAdmin(admin.ModelAdmin):  # Добовление в модель товаров модель с картинками в админке
    prepopulated_fields = {"slug": ("name",)}  # Транслирует текст написаный в name в slug
    list_display = ('name', 'warehouse', 'price')
    
    # Поле для добавления картинок товарам
    inlines = [
        ProductsImagesInLine,
    ]

    fieldsets = (
        ('Общее',
         {
             'fields': (('categories', 'manufacture'),)
         }
         ),
        ('Наименование',
         {
             'fields': (('name', 'slug'),)
         }
         ),
        ('Основное',
         {
             'fields': (('price', 'warehouse', 'warranty'),)
         }
         ),
        ('Описание',
         {
             'fields': (('description', 'specifications', 'set'),)
         }
         ),
        ('Постер',
         {
             'fields': (('slider', 'poster'),)
         }
         ),
    )


@admin.register(Category)  # Добовляю в админку модель с категориями товаров
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_image_category')
    prepopulated_fields = {"slug": ("name",)}  # Транслирует текст написаный в name в slug

    # Отображение картинки производиеля в таблице
    def get_image_category(self, product):
        # добавление HTML кода в стукруту таблицы в админке
        return mark_safe(f'<img src="{product.img.url}" alt="{product.name}" class="admin-icon"/>')

    get_image_category.short_description = u'Логотип категории'

    # Порядок отображения полей
    fieldsets = (
        ('Общее',
         {
             'fields': (('name', 'slug'), 'img')
         }
         ),
    )


@admin.register(Manufacture)  # Добовляю в админку модель с производителями
class ManufactureAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}  # Транслирует текст написаный в name в slug
    list_display = ('name', 'get_image')

    # Отображение картинки производиеля в таблице
    def get_image(self, product):
        # добавление HTML кода в стукруту таблицы в админке
        return mark_safe(f'<img src="{product.img.url}" alt="{product.name}" class="admin-icon manufacture"/>')

    get_image.short_description = u'Логотип'

    # Порядок отображения полей
    fieldsets = (
        ('Общее',
         {
             'fields': ('name', 'slug', 'country', 'img')
         }
         ),
    )


@admin.register(ProductsImage)
class ProductsImageAdmin(admin.ModelAdmin):
    pass
    
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
    # list_display = ("autor_name", "comment_text")

    # #Деактиаированые поля
    # readonly_fields =  ("autor_name", "comment_text")

    
    
    
    
    
    
    
    