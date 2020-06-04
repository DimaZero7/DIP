from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordResetView
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import  HttpResponse


class ChangePassword(SuccessMessageMixin, PasswordResetView):
    template_name = "authorization/change_password.html"
    success_url = "/authorization/login/"
    success_message = "Пароль изменен"


class Login(SuccessMessageMixin, LoginView):
    template_name = "authorization/login.html"
    success_message = "Привет"


class Logout(SuccessMessageMixin, LogoutView):
    next_page = "/"
    success_message = "Пока"

    
class Registration(SuccessMessageMixin, FormView):
    form_class = UserCreationForm
    success_url = "/authorization/login/"
    template_name = "authorization/register.html"
    
    
    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)
    
#    def form_invalid(self, form):
#        response = super(SuccessMessageMixin, self).form_invalid(form)
#        success_message = "Исправте ошибки"
#        return HttpResponse()
