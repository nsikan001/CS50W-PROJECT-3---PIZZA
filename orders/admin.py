from django.contrib import admin
from .models import ShoppingCart, Order, Category, Regular_pizza, Sicilian_pizza, Topping, Sub, Pasta, Salad, Dinner_platter

# Register your models here.


# class CategoryAdmin(admin.ModelAdmin):
#     list_display = ('name')
#
#
# class Regular_pizzaAdmin(admin.ModelAdmin):
#     list_display = ('name', 'small', 'large')
#
#
# class SubAdmin(admin.ModelAdmin):
#     list_display = ('name', 'small', 'large')


class ShoppingCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'prod_name', 'price', 'prod_qty', 'amount']


admin.site.register(Category)
admin.site.register(Regular_pizza)
admin.site.register(Sicilian_pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Dinner_platter)
admin.site.register(ShoppingCart)
admin.site.register(Order)