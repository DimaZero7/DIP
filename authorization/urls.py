from django.urls import path
from django.views.generic.base import RedirectView
from django.urls import path, include
from django.conf import settings

from .views import *

app_name = 'authorization'
#path('catalog/', include('catalog.urls')),
urlpatterns = [
    path('', RedirectView.as_view(url='/authorization/login/')),
    path('', include('social_django.urls', namespace='social')),
    path('login/', Login.as_view(), name='login'),
    path('change_password', ChangePassword.as_view(), name='change_password'),
    path('registration/', Registration.as_view(), name='registration'),
    path('logout/', Logout.as_view(), name='logout'),
]

