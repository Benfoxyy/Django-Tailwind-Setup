from django.urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'order'

urlpatterns = [
    path('',views.OrderCheckView.as_view(),name='order-check'),
    path('complete/',TemplateView.as_view(template_name='complete.html'),name='complete'),
]
