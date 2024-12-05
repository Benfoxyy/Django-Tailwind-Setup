from django.urls import path,re_path
from . import views

app_name = 'website'

urlpatterns = [
    path('',views.WebsiteHomeView.as_view(),name='home'),
    re_path(r'product/(?P<slug>[-\w]+)/detail/', views.ProductDetailVeiw.as_view(), name='product-detail'),
    path('product/add-to-cart/',views.AddToCart.as_view(),name='add-to-cart'),
]
