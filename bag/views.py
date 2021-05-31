from django.shortcuts import render

# Create your views here.

def bag_view(request):
    """ A view to render the shopping bag page """

    return render(request, 'bag/bag.html')