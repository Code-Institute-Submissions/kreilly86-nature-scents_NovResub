from django.shortcuts import render


def index(request):
    """A view to return index page"""
 
    return render(request, 'home/index.html')


def philosophy(request):
    """A view to return philosophy page"""

    return render(request, 'home/philosophy.html')


def subscription(request):
    """A view to return subscription page"""

    return render(request, 'home/subscription.html')
