from django.shortcuts import render
from apps.product.models import Product, Category

# Create your views here.
def frontpage(request):
    newest_products = Product.objects.all()[0:10]
    all_categories = Category.objects.all()

    template = 'core/frontpage.html'

    context = {
        'newest_products' : newest_products,
        'all_categories': all_categories,
    }

    return render(request, template, context)

def about(request):
    
    template = 'core/about.html'

    return render(request, template)


def contact(request):
    
    template = 'core/contact.html'

    return render(request, template)