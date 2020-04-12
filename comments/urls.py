from django.urls import path

from .views import *

app_name = 'comments'

urlpatterns = [
    path('comment_add/', comment_processing, name='treatment'),
]