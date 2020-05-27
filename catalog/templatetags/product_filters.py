from django import template

from manufacture.models import Manufacture


register = template.Library()


@register.simple_tag
def get_manufacture():
    """Выводит всех производителей"""
    return Manufacture.objects.all()
