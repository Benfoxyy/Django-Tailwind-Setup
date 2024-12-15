from django.views.generic import FormView,View
from django.http import JsonResponse
from django.urls import reverse_lazy
from .cart import CartSession
from .models import CartModel
from .forms import CartListForm
from payment.models import *

class CartListView(FormView):
    template_name = 'cart/cart.html'
    success_url = reverse_lazy('payment:complete')

    form_class = CartListForm
    def get_form_kwargs(self):
        kwargs = super(CartListView,self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs
    
    def form_valid(self, form):
        user = self.request.user
        coupon = form.cleaned_data['coupon_code']
        total_price = self.calculate_price(coupon)
        order = self.create_order(user,total_price)
        if coupon:
            self.add_coupon(user,order,coupon)
        self.add_product(order,user)
        return super().form_valid(form)
    

    def create_order(self,user,total_price):
        return OrderModel.objects.create(user=user,
                                         final_price=total_price)
    
    def add_coupon(self,user,order,coupon):
        order.coupon = coupon
        coupon.max_limit_usage -= 1
        coupon.used_by.add(user)
        coupon.save()
        order.save()

    def add_product(self,order,user):
        cart_items = CartModel.objects.get(user=user).cart_items.all()
        for product in cart_items:
            OrderItemsModel.objects.create(order=order,
                                           product=product.product,
                                           quantity=product.quantity,
                                           price=product.get_productprice())


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
        product_id = request.POST.get('product_id')
        if product_id:
            cart.add_prod(product_id,request.POST.get('quantity'))
        if request.user.is_authenticated:
            cart.cart_merge(request.user)
        return JsonResponse({'cart':cart.get_cart(),'total_quantity':cart.get_cart_quantity()})
    


class CheckView(View):
    def post(self, request, *args, **kwargs):
        coupon_code = request.POST.get('coupon_code')
        try:
            coupon = CouponModel.objects.get(code=coupon_code)
        except CouponModel.DoesNotExist:
            return JsonResponse({'message':'کد تخفیف یافت نشد'})
        else:
            if self.request.user in coupon.used_by.all():
                return JsonResponse({'message':'این کد توسط شما یک بار استفاده شده است'})
            if coupon.max_limit_usage == 0 :
                return JsonResponse({'message':'کد دیگر فاقد ارزش است'})
            else:
                cart = CartModel.objects.get(user=self.request.user)
                
                total_price = cart.calculate_total_price()
                
                discounted_price = total_price - (total_price/100 * coupon.discount_percent)

        return JsonResponse({'discounted_price':discounted_price,'message':'کد تخفیف با موفقیت ثبت شد'}) 