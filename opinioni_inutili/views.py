from django.shortcuts import render
from .models import Item

# Create your views here.
def home (request):
    items = Item.objects.all()
    return render(request, 'opinioni_inutili/home.html', {'items':items})

def contact_us(request):
    return render(request, 'opinioni_inutili/contact_us.html')

def login(request):
    return render(request, 'opinioni_inutili/login.html')

def register(request):
    return render(request, 'opinioni_inutili/register.html')

def seriously(request):
    return render(request, 'opinioni_inutili/seriously.html')