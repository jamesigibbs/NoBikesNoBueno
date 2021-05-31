from django.conf import settings


def bag_contexts(request):

    bag_items = []
    total = 0
    product_count = 0
    delivery = 10 #Want to make this configable in the admin
    
    grand_total = delivery + total

    context = {
        'bag_items': bag_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'grand_total': grand_total,
    }

    return context