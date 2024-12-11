from django.db import models

class CartModel(models.Model):
    user = models.ForeignKey("account.User",on_delete=models.CASCADE)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.user.email
    
    def calculate_total_price(self):
        return sum(prod.product.price * prod.quantity for prod in self.cart_items.all())
        
    
class CartItemModel(models.Model):
    cart = models.ForeignKey(CartModel,on_delete=models.CASCADE,related_name="cart_items") 
    product = models.ForeignKey('website.ProductModel',on_delete=models.PROTECT)
    quantity = models.PositiveIntegerField(default=0)
    
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.product.name} - {self.cart.id}"