from django import template
from django.db.models import Min, Max, Count
from django.db.models import Q

from manufacture.models import Manufacture
from catalog.models import Product

register = template.Library()


@register.simple_tag
def get_manufacture():
    """Выводит всех производителей"""
    return Manufacture.objects.all()


@register.simple_tag(takes_context=True)
def get_prise(context):
    """Выводит всех производителей"""
    object_list = context['object_list']
    return object_list.aggregate(min_prise=Min('price'), max_prise=Max('price'))
