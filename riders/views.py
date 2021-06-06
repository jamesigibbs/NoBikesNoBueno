from django.shortcuts import render

# Create your views here.

def riders(request):
    """A view to render rider bio page"""

    return render(request, 'riders/riders.html')
