from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ProductsImagesInLine(admin.TabularInline):  # Модель картинок в админке
    model = ProductsImage


class ProductsAdmin(admin.ModelAdmin):  # Добовление в модель товаров модель с картинками в админке
    prepopulated_fields = {"slug": ("name",)}  # Транслирует текст написаный в имя в слуг
    inlines = [
        ProductsImagesInLine,
    ]

    fieldsets = (
			('Общее',
				{
				'fields':(('categories','manufacture'),)
				}
			),
			('Наименование',
				{
				'fields':(('name','slug'),)
				}
			),
			('Основное',
				{
				'fields':(('price','warehouse','warranty'),)
				}
			),
			('Описание',
				{
				'fields':('description','specifications', 'complect')
				}
			),
#            ('Акция',
#				{
#				'fields':('action','poster')
#				}
#			),
	)
    
admin.site.register(Category)  # Добовляю в админку модель с категориями товаров
admin.site.register(Product, ProductsAdmin)  # Добовляю в админку модель с категориями товаров


@admin.register(Manufacture) # Добовляю в админку модель с производителями
class ManufactureAdmin(admin.ModelAdmin):
	list_display = ( 'get_image', 'name')

    #Отображение картинки производиеля в таблице
	def get_image(self, product):
        #добавление HTML кода в стукруту таблицы в админке
		return mark_safe(f'<img src="{product.img.url}" alt="{product.name}" style="width: 30px"/>')
    
	get_image.short_description = u'Логотип'
# alt="{product.manufacture.name}" title="{product.manufacture.name}"
    #Порядок отображения полей
	fieldsets = (
			('Общее',
				{
				'fields':('name', 'country', 'img')
				}
			),
	)
