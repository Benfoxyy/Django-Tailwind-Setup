from django.urls import path
from . import views

app_name = 'payment'

urlpatterns = [
    path('complete/',views.PaymentCompleteView.as_view(),name='complete'),
    path('verify',views.VerificationView.as_view(),name='cart-summery'),
]
