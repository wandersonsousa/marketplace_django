from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'core/index.html')

def contact(request):
    return render(request, 'core/contact.html')

def about(request):
    return render(request, 'core/about.html')

def terms_of_use(request):
    return render(request, 'core/terms-of-use.html')

def privacy(request):
    return render(request, 'core/privacy.html')