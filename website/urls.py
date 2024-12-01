from django.urls import path
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.WebsiteHomeView.as_view(),name='home'),
]
