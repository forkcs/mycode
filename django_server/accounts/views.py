from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import FormView

from django_server.accounts.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = 'admin/'


class LogInView(LoginView):
    template_name = 'accounts/login.html'


class LogOutView(LogoutView):
    pass
