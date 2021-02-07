from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import User
from .models import Vendor
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

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
    
    template = 'vendor/vendor_admin.html'
    
    context = {
        'vendor' : vendor,
    }
    return render(request, template, context)    