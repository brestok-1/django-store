from django.shortcuts import render
from .models import *


# Create your views here.
def index(request):
    context = {
        'title': 'Store'
    }
    return render(request, 'products/index.html', context)


def products(request):
    context = {
        'title': 'Store - Catalog',
        'products': Product.objects.all(),
        'category': ProductCategory.objects.all(),
    }
    return render(request, 'products/products.html', context)
