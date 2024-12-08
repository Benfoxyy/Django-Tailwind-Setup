from django.views.generic import FormView,View
from django.http import JsonResponse
from django.urls import reverse_lazy
from .cart import CartSession
from .forms import CartListForm

class CartListView(FormView):
    template_name = 'cart/cart.html'
    success_url = reverse_lazy('order:complete')

    form_class = CartListForm
    # success_url = reverse_lazy('order:complete')
    def get_form_kwargs(self):
        kwargs = super(CartListView,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        coupon = form.cleaned_data['coupon_code']
        total_price = self.calculate_price(coupon)
        print(total_price)
        return super().form_valid(form)


    def get_template_names(self):
        cart = CartSession(self.request.session)
        if not cart.get_cart_items():
            return ["cart/empty-cart.html"]
        return super().get_template_names()
    
    def calculate_price(self,coupon):
        cart = CartSession(self.request.session)
        if coupon:
            return cart.get_total_price(coupon.discount_percent)
        else:
            return cart.get_total_price()
        
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart = CartSession(self.request.session)
        context['cartlist'] = cart.get_cart_items()
        context['total_quantity'] = cart.get_cart_quantity()
        context['total_price'] = cart.get_total_price()
        return context
    

class CartAddProductView(View):
    def post(self, request, *args, **kwargs):
        cart = CartSession(request.session)
        if product_id := request.POST.get('product_id'):
            cart.add_prod(product_id)
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse({'cart':cart.get_cart(),'total_quantity':cart.get_cart_quantity()})