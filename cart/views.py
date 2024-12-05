from django.views.generic import TemplateView,View
from django.http import JsonResponse
from .cart import CartSession

class CartListView(TemplateView):
    template_name = 'cart/cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        context['cartlist'] = cart.get_cart_items()
        context['total_quantity'] = cart.get_cart_quantity()
        return context
    

class CartAddProductView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        if product_id := request.POST.get('product_id'):
            cart.add_prod(product_id)
        # if request.user.is_authenticated:
        #     cart.cart_merge(request.user)
        return JsonResponse({'cart':cart.get_cart(),'total_quantity':cart.get_cart_quantity()})