from django.shortcuts import render, redirect
from django.core.mail import send_mail
from apps.product.models import Product, Category
from django.contrib.auth.models import User
from django.contrib import messages
from apps.contact.models import Contact
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


