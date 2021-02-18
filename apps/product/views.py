import random
from django.db.models import Q

from django.shortcuts import render, get_object_or_404,redirect
from django.core.paginator import   EmptyPage, PageNotAnInteger, Paginator
from .models import Category, Product, Photo, ProductReview


# Create your views here.
def search(request):
    query = request.GET.get('query', '')
    products = Product.objects.filter(Q(title__icontains=query) | Q(description__icontains=query))

    return render(request, 'product/search.html', {'products': products, 'query': query})


def gallery(request):
    category = request.GET.get('category')

    if category == None:
        photos = Product.objects.all()
    else:
        photos = Product.objects.filter(category__title=category)

    categories = Category.objects.all()
    paginator = Paginator(photos, 3)
    page = request.GET.get('page')
    paged_photos = paginator.get_page(page)

    context = {'categories': categories, 'photos': paged_photos}
    return render(request, 'product/gallery.html', context)


def viewPhoto(request, pk):
    photo = Product.objects.get(id=pk)

    # Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', '' )
        content = request.POST.get('content', '')
        name= request.POST.get('name', '')

        review = ProductReview.objects.create(product=photo, user=request.user, stars=stars, content=content, name=name)

        return redirect('photo', pk=pk )

    #

    return render(request, 'product/photos.html', {'photo': photo})

def product(request, category_slug, product_slug):
    product = get_object_or_404(Product, category__slug=category_slug, slug=product_slug)
    photo = Product.objects.get(category__slug=category_slug, slug=product_slug)
    

    # Add review

    if request.method == 'POST' and request.user.is_authenticated:
        stars = request.POST.get('stars', '' )
        content = request.POST.get('content', '')
        name= request.POST.get('name', '')

        review = ProductReview.objects.create(product=product, user=request.user, stars=stars, content=content, name=name)

        return redirect('product', category_slug=category_slug, product_slug=product_slug)

    #

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

