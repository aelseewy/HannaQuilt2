from django.shortcuts import render, redirect
from django.core.mail import send_mail
from apps.product.models import Product, Category
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.
def frontpage(request):
    newest_products = Product.objects.all()[0:7]
    all_categores = Category.objects.filter(is_selected=True)
    
    all_categories = Category.objects.filter(is_active=True)

    template = 'core/frontpage.html'

    context = {
        'newest_products' : newest_products,
        'all_categories': all_categories,
        'all_categores' : all_categores,
    }

    return render(request, template, context)

def about(request):
    
    template = 'core/about.html'

    return render(request, template)


def contact(request):
    if request.method == 'POST':
        quilt_listing = request.POST['quilt_listing']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        


        if request.user.is_authenticated:
            user_id = request.user.id
        send_mail(
                'New Quilt Contact',
                'You have a new contact message for the quilt ' + quilt_listing + message +'. Please login to your admin panel for more info.  ' + message, 
                'quiltinegypt@gmail.com',
                [email],
                fail_silently=False,
            )

        
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('contact')
    template = 'core/contact.html'

    return render(request, template)