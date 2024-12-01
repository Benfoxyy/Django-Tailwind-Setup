from django.views.generic import ListView
from .models import ProductModel

class WebsiteHomeView(ListView):
    template_name = 'website/index.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'products'
    