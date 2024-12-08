from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class OrderStatusModel(models.IntegerChoices):
    pending = 1 , 'در انتظار پرداخت'
    success = 2 , 'موفقیت آمیز'
    faild = 3 , 'لغو شده'

class CouponModel(models.Model):
    code = models.CharField(max_length=100)
    discount_percent = models.IntegerField(default=0,validators=[MinValueValidator(0), MaxValueValidator(100)])
    max_limit_usage = models.IntegerField(default=10)
    used_by = models.ManyToManyField('account.User', blank=True)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderModel(models.Model):
    user = models.ForeignKey('account.User',on_delete=models.PROTECT)
    coupon = models.OneToOneField(CouponModel,on_delete=models.PROTECT,blank=True,null=True)
    status = models.IntegerField(choices=OrderStatusModel.choices,default=OrderStatusModel.pending.value)
    final_price = models.DecimalField(default=0,max_digits=10,decimal_places=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

class OrderItemsModel(models.Model):
    order = models.ForeignKey(OrderModel, on_delete=models.CASCADE)
    product = models.ForeignKey('website.ProductModel', on_delete=models.PROTECT)
    quantity = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=10,decimal_places=0)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)