from django.contrib import admin

from .models import Category, Product, Photo, ProductReview

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Photo)
admin.site.register(ProductReview)