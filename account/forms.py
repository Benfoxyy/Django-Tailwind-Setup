from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User

class AccountLoginForm(AuthenticationForm):
    def confirm_login_allowed(self, user):
        super(AccountLoginForm,self).confirm_login_allowed(user)

class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']