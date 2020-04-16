from django.urls import path
from django.conf.urls import include, url
from .views import *

app_name = 'auth'

urlpatterns = [
    path('', LoginFormView.as_view(), name='login'),
    path('login/', LoginFormView.as_view(), name='login'),
    path('reg/', RegisterFormView.as_view(), name='reg'),
    path('logout/', LogoutView.as_view(), name='logout'),
]

