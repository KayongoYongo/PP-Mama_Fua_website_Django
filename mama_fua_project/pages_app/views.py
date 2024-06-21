from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request, 'pages_app/index.html')

def location_page(request):
    return render(request, 'pages_app/our_location.html')

def contact_page(request):
    return render(request, 'pages_app/contact.html')