from django.shortcuts import render

def view_cart(request):
    """A view to view the shopping cart """
    
    return render(request, 'shopping_cart/cart.html')
