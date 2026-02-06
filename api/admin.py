from django.contrib import admin
from api.models import Order, OrderItem, Product, User

# Register your models here.

class OrderItemInline(admin.TabularInline):
    model= OrderItem

class UserAdmin(admin.ModelAdmin):
    model= User

class ProductAdmin(admin.ModelAdmin):
    model= Product

class OrderAdmin(admin.ModelAdmin):
    inlines =[
        OrderItemInline
    ]

admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)