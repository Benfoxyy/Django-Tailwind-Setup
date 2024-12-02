from django.db import models
from django.utils.translation import gettext_lazy as _

class ProductCategoryModel(models.IntegerChoices):
    Apartemani = 1, _('آپارتمانی')
    Tazini = 2, _('تزینی')
    Kadoe = 3, _('کادویی')

class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True,unique=True)
    price = models.DecimalField(decimal_places=0,max_digits=10,default=0)
    stock = models.PositiveIntegerField(default=0)
    category = models.IntegerField(choices=ProductCategoryModel.choices)
    image = models.ImageField(default='default/product-default.png',upload_to='products/')

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name