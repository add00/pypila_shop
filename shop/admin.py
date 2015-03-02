from django.contrib import admin

from shop.models import Product, Order, OrderPosition


admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderPosition)
