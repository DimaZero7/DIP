from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category, Product, ProductsImage
from poster.admin import PosterInLine


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Представление интерфейса категорий"""

    search_fields = ['name']

    def get_image(self, Category):
        """Добавление HTML кода ( изоброжение категории ) в стукруту таблицы в админке"""

        return mark_safe(f'<img src="{Category.img.url}" alt="{Category.name}" class="admin-icon"/>')

    get_image.short_description = u'Логотип'
    list_display = ('name', 'get_image')

    fieldsets = [
        ('Наименование категории', {'fields': ['name', 'slug']}),
        ('Изоброжение', {'fields': ['img']})
    ]

    prepopulated_fields = {"slug": ("name",)}


class ProductsImagesInLine(admin.TabularInline):
    """Предстовление о картинках товаров"""

    model = ProductsImage


@admin.register(Product)
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

    list_filter = ('categories', 'manufacture')


