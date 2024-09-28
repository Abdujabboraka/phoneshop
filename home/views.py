from django.shortcuts import render
from .models import Category, Phone
# Create your views here.

def home(request):
    categories = Category.objects.all()
    phones = Phone.objects.all()
    context = {
        'categories': categories,
        'phones': phones
    }
    return render(request, 'home.html', context)
