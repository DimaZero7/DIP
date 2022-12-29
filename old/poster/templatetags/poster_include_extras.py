from django import template

from poster.models import Poster


register = template.Library()


@register.simple_tag()
def get_poster():
    """Выдаёт 5 последних обетов которые должны находиться в постере"""
    return Poster.objects.filter(slider=True).order_by('id')[:5]
