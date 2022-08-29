from django.shortcuts import render, redirect


def cart(request):
    """A view to see the contents of customer shopping cart """

    return render(request, 'shopping_cart/cart.html',)


def add_to_cart(request, item_id):
    """Add products to the shopping cart"""

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    return redirect(redirect_url)
