from django.urls import path
from . import views

app_name = 'authorization'

urlpatterns = [
    # /
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
] 
