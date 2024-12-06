from django.contrib import admin
from .models import CartModel,CartItemModel

admin.site.register(CartModel)
admin.site.register(CartItemModel)