from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('profile/<int:pk>/',views.DashboardProfileView.as_view(),name='profile'),
]
