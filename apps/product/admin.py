from django.contrib import admin

from .models import Category, Product, Photo

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Photo)