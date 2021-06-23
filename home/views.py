from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from home.models import Product

from django.db.models.functions import Lower


def home(request):
    """ A view to render index.html and products in to cards"""
    products = Product.objects.all()
    query = None
    sort = None
    direction = None
    nav = 'home'

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, 'No search criteria found!')
                return redirect(reverse('home'))
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_sorting': current_sorting,
        'nav': nav,
    }

    return render(request, 'home/index.html', context)


def add_one_to_bag(request, item_id):
    """ Add an item to the shopping bag """
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += 1
    else:
        bag[item_id] = 1

    messages.success(request, 'Item added to cart')
    request.session['bag'] = bag
    return redirect(reverse('home'))


def product(request, product_id):
    """ A view to show more details on the each product """
    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'home/product.html', context)

