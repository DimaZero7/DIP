from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeDoneView, PasswordResetView


class ChangePassword(PasswordResetView):
    template_name = "authorization/change_password.html"
    success_url = "/authorization/login/"


class Login(LoginView):
    template_name = "authorization/login.html"


class Logout(LogoutView):
    next_page = "/"


class Registration(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "authorization/register.html"
    
    def form_valid(self, form):
        form.save()
        return super(Registration, self).form_valid(form)

