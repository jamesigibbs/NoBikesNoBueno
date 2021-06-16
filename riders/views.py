from django.shortcuts import render
from riders.models import Rider

# Create your views here.

def riders(request):
    """A view to render rider bio page"""
    riders = Rider.objects.all()
    nav = 'riders'

    context = {
        'riders': riders,
        'nav': nav,
    }

    return render(request, 'riders/riders.html', context)
