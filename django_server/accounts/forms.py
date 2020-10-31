from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UsernameField
from django.forms import ModelForm, CharField, ValidationError

from django_server.accounts.models import Account

User = get_user_model()

LoginForm = AuthenticationForm


class RegisterForm(ModelForm):
    class Meta:
        model = Account
        fields = '__all__'
        exclude = 'user',

    username = UsernameField()
    password1 = CharField(min_length=8, required=True)
    password2 = CharField(min_length=8, required=True)

    def save(self, commit=True):
        password = self.cleaned_data.pop('password1')
        if password != self.cleaned_data.pop('password2'):
            raise ValidationError('Пароли должны совпадать!')
        username = self.cleaned_data.pop('username')

        new_user = User.objects.create(username=username)
        new_user.set_password(password)
        new_user.save()

        Account.objects.create(**self.cleaned_data)
