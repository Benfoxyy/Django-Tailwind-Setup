from django import forms
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import AuthenticationForm,UserCreationForm
from .models import User

class AccountLoginForm(AuthenticationForm):
    error_messages = {
        "invalid_login": (
            "ایمیل یا رمز عبور اشتباه است"
        ),
        "inactive": _("This account is inactive."),
    }

class AccountRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']