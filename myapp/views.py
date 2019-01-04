from django.shortcuts import render


# Create your views here.
def index(request):
    """The home page for myapp"""
    return render(request, 'myapp/index.html')
