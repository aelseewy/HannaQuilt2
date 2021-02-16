from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact
from django.core.mail import send_mail
from django.contrib.auth.models import User
from apps.vendor.models import Vendor

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        quilt_id = request.POST['quilt_id']
        quilt_title = request.POST['quilt_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']


        if request.user.is_authenticated:
            
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(quilt_id=quilt_id, user_id=user_id)
            if has_contacted:
                messages.error(request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/photo/'+quilt_id)

        contact = Contact(quilt_id=quilt_id, quilt_title=quilt_title, user_id=user_id,
        first_name=first_name, last_name=last_name, email=email, phone=phone, message=message)
        contact.save()
        
        user_name = request.user.First_Name
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        
        send_mail(
                'New Quilt Inquiry',
                'You have a new inquiry for the quilt ' + quilt_title + user_name + '. Please login to your admin panel for more info.',
                'quiltinegypt@gmail.com' ,
                [email],
                fail_silently=False,
            )

        
        messages.success(request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/photo/'+quilt_id)
    

    