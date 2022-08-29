from django.shortcuts import render

def view_cart(request):
    """A view to see the contents of customer shopping cart """
    
    return render(request, 'shopping_cart/cart.html')
