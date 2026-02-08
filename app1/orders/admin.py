from django.contrib import admin

# Register your models here.
from orders.models import Order, CartItem

admin.site.register(Order)
admin.site.register(CartItem)