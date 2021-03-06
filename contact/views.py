from django.shortcuts import render
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

import os

if os.path.exists("env.py"):
    import env


def contact_view(request):
    """ A view to render the shopping bag page """
    name = None
    email = None
    subject = None
    message = None
    sub_for_recipient = None
    nav = 'contact'
    context = {
        'nav': nav
    }
    context_email = {}

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        if subject is None:
            sub_for_recipient = f'Message from - {name}'
        else:
            sub_for_recipient = f'{subject} - {name}'

        user_msg = render_to_string(
            'contact/emails/user_email.txt',
            {'name': name, },
            )
        nbnb_msg = render_to_string(
            'contact/emails/nbnb_email.txt',
            {'name': name, 'message': message, 'email': email, },
                                        )

        context_email = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        # Email to NBNB
        NBNBemail = EmailMessage(
            sub_for_recipient,
            nbnb_msg,
            email,
            [os.environ.get("EMAIL_HOST_USER")],
            reply_to=[email],
        )

        NBNBemail.send()

        # Email to User
        send_mail(
            'No Bikes No Bueno',
            user_msg,
            os.environ.get("EMAIL_HOST_USER"),
            [email],
        )

        context.update(context_email)

    else:
        context_email: {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }

        context.update(context_email)

    return render(request, 'contact/contact.html', context)
