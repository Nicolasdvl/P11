from django.contrib import admin

from .models import Product, Category, Claim

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Claim)
