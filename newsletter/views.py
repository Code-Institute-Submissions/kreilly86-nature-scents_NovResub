from django.shortcuts import redirect
from .models import NewsletterInput
from django.contrib import messages


def newsletter_signup(request):
    
    if request.method == 'POST':
        email = request.POST.get('email')

        input = NewsletterInput(email=email)
        input.save()

    return redirect('home')
