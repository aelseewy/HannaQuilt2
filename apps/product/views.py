import random
from django.shortcuts import render, get_object_or_404

from .models import Category, Product, Photo


# Create your views here.
def gallery(request):
    category = request.GET.get('category')
    if category == None:
        photos = Product.objects.all()
    else:
        photos = Product.objects.filter(category__title=category)

    categories = Category.objects.all()
    context = {'categories': categories, 'photos': photos}
    return render(request, 'product/gallery.html', context)


def viewPhoto(request, pk):
    photo = Product.objects.get(id=pk)
    return render(request, 'product/photos.html', {'photo': photo})

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    photo = Product.objects.get(category__slug=category_slug, slug=product_slug)

    similar_products = list(product.category.products.exclude(id=product.id))

    if len(similar_products) >= 4:
        similar_products = random.sample(similar_products, 4)
    template = 'product/product.html'

    context = {
        'product': product, 
        'photo': photo,
        'similar_products': similar_products, 
    }
    
    return render(request, template, context)

def category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)

    template = 'product/category.html'

    context = {
        'category' : category,
    }
    return render(request, template, context)