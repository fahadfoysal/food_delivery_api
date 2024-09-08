from django.contrib import admin
from .models import Resturant, Category, Menu, Item, Modifier, Order, OrderItem

admin.site.register(Resturant)
admin.site.register(Category)
admin.site.register(Menu)
admin.site.register(Item)
admin.site.register(Modifier)
admin.site.register(Order)
admin.site.register(OrderItem)
