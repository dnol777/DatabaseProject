from django.shortcuts import render
from django.utils import timezone
from .models import Product

# Create your views here.

def product_list(request):
    products = Product.objects.all()
    return render(request, 'table/product_list.html', {'products': products})
