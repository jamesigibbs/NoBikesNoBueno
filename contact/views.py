from django.shortcuts import render
from django.core.mail import send_mail

import os

if os.path.exists("env.py"):
    import env

# Create your views here.

def contact_view(request):
    """ A view to render the shopping bag page """
        
    name = None
    email =  None
    subject = None
    message =  None
    sub_for_recipient = None
    context = {}

    if request.method == 'POST':
        name = request.POST['name']
        email =  request.POST['email']
        subject = request.POST['subject']
        message =  request.POST['message']
        
        if subject == None:
            sub_for_recipient = f'Message from - {name}'
        else: 
            sub_for_recipient = f'{subject} - {name}'

        context = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        send_mail(
            sub_for_recipient,
            message,
            email,
            [os.environ.get("EMAIL_HOST_USER")],
        )

    else:
        context: {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
    return render(request, 'contact/contact.html', context)
