from django.contrib import admin
from .models import Products, Catagories, Customer, Order, OrderItem, ShippingAddress

# Register your models here.
admin.site.register(Catagories)
admin.site.register(Products)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)


