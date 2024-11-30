from django.urls import path
from . import views

app_name = 'account'

urlpatterns = [
    path('register/',views.AccountRegisterView.as_view(),name='register'),
    path('login/',views.AccountLoginView.as_view(),name='login'),
    path('logout/',views.AccountLogOutView.as_view(),name='logout'),
]
