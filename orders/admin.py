from django.contrib import admin
from .models import Pizza, Topping, Sub, Pasta, Salad, Platter, Cart, Order

# Register your models here.
admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Sub)
admin.site.register(Pasta)
admin.site.register(Salad)
admin.site.register(Platter)
admin.site.register(Cart)
admin.site.register(Order)