from django import forms
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User

class AccountLoginForm(AuthenticationForm):
    pass

class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField(required=False)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']