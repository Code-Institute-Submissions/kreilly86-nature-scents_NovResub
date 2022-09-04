from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm


def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your shopping cart at the moment")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51LF1WADrSNql7Q22hPSmaVGPS1RdvsGvKZ9ZthlkZSXTsCSIKMsFcRPs2E1hhgKKjK9iolu4HTkQk1QIi9yrK9I7002PgbmapI'
        ,
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
