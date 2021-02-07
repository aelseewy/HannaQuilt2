from django.shortcuts import render

# Create your views here.
def frontpage(request):

    template = 'core/frontpage.html'

    return render(request, template)

def about(request):
    
    template = 'core/about.html'

    return render(request, template)

def service(request):
    
    template = 'core/service.html'

    return render(request, template)

def contact(request):
    
    template = 'core/contact.html'

    return render(request, template)