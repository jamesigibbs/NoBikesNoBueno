from django.shortcuts import render
from home.models import Product
# Create your views here.


def index(request):
    """ A view to render index.html and products in to cards"""
    products = Product.objects.all

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
