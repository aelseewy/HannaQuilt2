from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Vendor
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from apps.product.models import Product, Category
from apps.vendor.models import Vendor
from .forms import ProductForm
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from apps.contact.models import Contact
from django.core.mail import send_mail
from django.core.paginator import   EmptyPage, PageNotAnInteger, Paginator
# Create your views here.
def become_vendor(request):
    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
 
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists!')
                return redirect('become_vendor')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists!')
                    return redirect('become_vendor')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name= lastname, email=email, username=username, password=password)
                    auth.login(request, user)
                    messages.success(request, 'You are now logged in.')
                    vendor = Vendor.objects.create(name=user.username, created_by=user)
                    return redirect('frontpage')
                    user.save()
                    messages.success(request, 'You are registered successfully.')
                    vendor = Vendor.objects.create(name=user.username, created_by=user)
                    return redirect('become_vendor')
        else:
            messages.error(request, 'Password do not match')
            return redirect('become_vendor')
    else:
        return render(request, 'vendor/become_vendor.html')



    template = 'vendor/become_vendor.html'

    return render(request, template)

@login_required
def vendor_admin(request):
    vendor = request.user.vendor
    products = vendor.products.all()
    productss = vendor.products.all()
    paginator = Paginator(productss, 3)
    page = request.GET.get('page')
    paged_productss = paginator.get_page(page)    

    template = 'vendor/vendor_admin.html'
    
    context = {
        'vendor' : vendor,
        'products' : products,
        'productss': paged_productss,
    }
    return render(request, template, context)

@login_required
def add_product(request):

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)

        if form.is_valid():
            product = form.save(commit=False)
            product.vendor = request.user.vendor
            product.slug = slugify(product.title)
            product.save()

            return redirect('vendor_admin')
    else:
        form = ProductForm()
    
    return render(request, 'vendor/add_product.html', {'form': form})

@login_required
def myinquiries(request):
    vendor = request.user.vendor
    myinquiry = Contact.objects.all().filter(user_id=request.user.id)
    paginator = Paginator(myinquiry, 3)
    page = request.GET.get('page')
    paged_myinquiry = paginator.get_page(page)    

    context = {
        'vendor': vendor,
        'myinquiries': paged_myinquiry,
        
    }
    return render(request, 'vendor/inquirieslist.html', context)

@login_required
def inquiry1(request):
    vendor = request.user.vendor
    myinquiry = Contact.objects.all().filter(owner_id=request.user.vendor.id)
    paginator = Paginator(myinquiry, 3)
    page = request.GET.get('page')
    paged_myinquiry = paginator.get_page(page)
    
    context = {
        'vendor' : vendor,
        'inquiries': paged_myinquiry,
        
    }
    return render(request, 'vendor/dashboard_inquiries.html', context)

@login_required
def send_reply(request):
    if request.method =="POST":
        email = request.POST['email']
        message = request.POST['message']
        quilt_listing = request.POST['quilt_listing']
        send_mail(
            'Reply from ' + quilt_listing + ' owner',
            message,
            'sewemallonline@gmail.com',
            [email],
            fail_silently=False
        )
        messages.success(request, 'Your reply has been sent successfully')
        return redirect('myinquiries')
    else:
        return redirect('vendor_admin')
