from django.contrib.auth.views import LoginView, LogoutView
from django.core.exceptions import ValidationError
from django.views.generic import FormView

from django_server.accounts.models import Account
from django.contrib.auth.models import User
from django_server.accounts.forms import RegisterForm


class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/admin/'


class LogInView(LoginView):
    template_name = 'accounts/login.html'
    success_url = '/admin/'
    redirect_authenticated_user = False

    def form_valid(self, form):
        password = form.cleaned_data.pop('password1')
        if password != form.cleaned_data.pop('password2'):
            raise ValidationError('Пароли должны совпадать!')
        username = form.cleaned_data.pop('username')

        new_user = User.objects.create_user(username=username, password=password)

        Account.objects.create(new_user, **form.cleaned_data)
        return super(LogInView, self).form_valid(form)


class LogOutView(LogoutView):
    pass
