from django.shortcuts import render
from .models import Product
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def home(request):
    products = Product.objects.all()

    return render(request, 'ecommerce/home.html', {'products': products})


def register(request):
    return render(request, 'registration/register.html')
