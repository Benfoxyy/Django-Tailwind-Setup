from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    path('',views.CartListView.as_view(),name='cart-list'),
    path('<int:pk>/add/',views.CartAddProductView.as_view(),name='cart-add'),
    path('check/',views.CheckView.as_view(),name='check'),
]
