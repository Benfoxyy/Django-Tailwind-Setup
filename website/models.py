from django.db import models

class ProductModel(models.Model):
    name = models.CharField(max_length=250)
    slug = models.SlugField(allow_unicode=True,unique=True)
    price = models.DecimalField(decimal_places=0,max_digits=10,default=0)
    stock = models.PositiveIntegerField(default=0)
    image = models.ImageField(default='default/product-default.png',upload_to='products/')

    def __str__(self):
        return self.name