from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Manufacture


class ManufactureAdmin(admin.ModelAdmin):
    """Предстовление модели производителей в админке"""

    prepopulated_fields = {"slug": ("name",)}

    def get_image(self, Manufacture):
        """Добавляем картинку производителей в список в админке"""

        return mark_safe(f'<img src="{Manufacture.img.url}" alt="{Manufacture.name}" class="admin-icon manufacture"/>')

    list_display = ('name', 'get_image')

    get_image.short_description = u'Логотип'

    fieldsets = [
        ('Общее', {'fields': ['name', 'slug', 'country', 'img']}),
    ]


admin.site.register(Manufacture, ManufactureAdmin)
