from django.contrib.auth.views import LoginView,LogoutView
from django.contrib.auth import login
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import AccountLoginForm,AccountRegisterForm

class AccountRegisterView(SuccessMessageMixin,FormView):
    template_name = 'account/register.html'
    form_class = AccountRegisterForm
    success_url = '/'
    success_message = 'ثبت نام کاربر با موفقیت انجام شد'

    def form_valid(self, form):
        user = form.save()
        login(self.request,user)
        return super().form_valid(form)
    
    
class AccountLoginView(SuccessMessageMixin,LoginView):
    template_name = 'account/login.html'
    form_class = AccountLoginForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('website:home')
    success_message = 'کاربر با موفقیت وارد شد'

class AccountLogOutView(LogoutView):
    pass

    