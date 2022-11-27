from django.shortcuts import redirect
from django.contrib import messages
from .models import NewsletterInput


def newsletter_signup(request):

    if request.method == 'POST':
        email = request.POST.get('email')

        input = NewsletterInput(email=email)
        input.save()
        messages.success(request, 'Thanks for subscribing!')

    return redirect('home')
