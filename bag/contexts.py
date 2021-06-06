from django.conf import settings
from django.shortcuts import get_object_or_404
from home.models import Product


def bag_contexts(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 10 # Want to make this configable in the admin
    bag = request.session.get('bag', {})
    
    for item_id, quantity in bag.items():
        product = get_object_or_404(Product, pk=item_id)
        total += quantity * product.price
        product_count += quantity
        print(product)
        bag_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
        })

    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context