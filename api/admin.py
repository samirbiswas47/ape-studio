from django.contrib import admin
from api.models import Order, OrderItem, Product, User

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model= OrderItem

class ProductAdmin(admin.ModelAdmin):
    model= Product

class OrderAdmin(admin.ModelAdmin):
    inlines =[
        OrderItemInline
    ]

admin.site.register(User)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)