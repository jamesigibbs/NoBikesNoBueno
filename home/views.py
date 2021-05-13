from django.shortcuts import render, get_object_or_404
from home.models import Product
# Create your views here.


def index(request):
    """ A view to render index.html and products in to cards"""
    products = Product.objects.all

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)


def product(request, product_id):
    """ A view to show more details on the each product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'home/product.html', context)

