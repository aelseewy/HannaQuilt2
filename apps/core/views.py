from django.shortcuts import render
from apps.product.models import Product

# Create your views here.
def frontpage(request):
    newest_products = Product.objects.all()[0:4]

    template = 'core/frontpage.html'

    context = {
        'newest_products' : newest_products,
    }

    return render(request, template, context)

def about(request):
    
    template = 'core/about.html'

    return render(request, template)

def service(request):
    
    template = 'core/service.html'

    return render(request, template)

def contact(request):
    
    template = 'core/contact.html'

    return render(request, template)