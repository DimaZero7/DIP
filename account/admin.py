from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):

    list_display = ('user', 'city', 'street', 'number_house', 'number_room')