from django.contrib import admin
from .models import *

admin.site.register(OrderModel)
admin.site.register(OrderItemsModel)
admin.site.register(CouponModel)

@admin.register(PaymentModel)
class PaymentModelAdmin(admin.ModelAdmin):
    list_display = (
        "id",
        "authority",
        "amount",
        "status",
        "created_date"
    )