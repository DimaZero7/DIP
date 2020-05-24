from django import template

from catalog.models import Category


register = template.Library()


@register.simple_tag()
def get_categories():
    """Выдает все каткгории"""
    return Category.objects.all()