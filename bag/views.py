from django.shortcuts import render, redirect, reverse, HttpResponse

# Create your views here.

def bag_view(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add an item to the shopping bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag

    return redirect(redirect_url)


def adjust_bag(request, item_id):
    """ Adjust an item in the shopping bag """

    quantity = int(request.POST.get('quantity'))
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    if quantity > 0:
        bag[item_id] = quantity
    else:
        bag.pop(item_id)

    request.session['bag'] = bag

    return redirect(reverse('bag_view'))


def remove_item(request, item_id):
    """ Add an item to the shopping bag """
    try:
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
        else:
            bag[item_id] = quantity

        if quantity > 0:
            quantity = 0
            bag[item_id] = quantity
        else:
            bag.pop(item_id)

        request.session['bag'] = bag

        return HttpResponse(status=200)
    except:
        return HttpResponse(status=500)
