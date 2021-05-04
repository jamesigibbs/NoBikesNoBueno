from django.shortcuts import render
from products.models import Product
# Create your views here.


def index(request):
    """ A view to render index.html """
    
    products = Product.objects.all

    context = {
        'products': products,
    }

    return render(request, 'home/index.html', context)
