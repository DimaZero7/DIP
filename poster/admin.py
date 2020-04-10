from django.contrib import admin

from .models import Poster


class PosterInLine(admin.TabularInline):
    """Предстовление о постере в админке"""

    model = Poster

