from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import Newsletter


def newsletter_list(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        entry = Newsletter(email=email)
        entry.save()

    return redirect('home')
