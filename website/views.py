from django.views.generic import ListView,DetailView,View
from django.http import JsonResponse
from .models import ProductModel,ProductCategoryModel
from cart.cart import CartSession

class WebsiteHomeView(ListView):
    template_name = 'website/index.html'
    queryset = ProductModel.objects.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["Apartemani"] = self.queryset.filter(category = ProductCategoryModel.Apartemani.value)
        context["Tazini"] = self.queryset.filter(category = ProductCategoryModel.Tazini.value)
        context["Kadoe"] = self.queryset.filter(category = ProductCategoryModel.Kadoe.value)
        return context
    

class ProductDetailVeiw(DetailView):
    template_name = 'website/product-detail.html'
    queryset = ProductModel.objects.all()
    context_object_name = 'product' 