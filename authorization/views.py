from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout


#Регестрация
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/"
    template_name = "register.html"
    
    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

#Аторизация
class LoginFormView(FormView):
    form_class = AuthenticationForm
    template_name = "login.html"
    success_url = "/account"
    
    def form_valid(self, form):
        self.user = form.get_user()
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

#Выход
class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")
    