from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Category


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


admin.site.register(Category, CategoryAdmin)
