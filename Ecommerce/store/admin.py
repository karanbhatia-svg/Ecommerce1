from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.orders import OrderItem
from .models.orders import Order

# Register your models here.


class AdminProduct(admin.ModelAdmin):
    list_display = ['name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(Product, AdminProduct)
admin.site.register(Category , AdminCategory)
admin.site.register(OrderItem )
admin.site.register(Order )
