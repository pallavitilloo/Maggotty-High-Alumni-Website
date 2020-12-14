from Maggotty.models import Order

def get_current_cart_to_context(request):
    current_user = request.user
    cart_items = 0 
    cart_items = Order.objects.filter(username=current_user.username,ifPaid=False).count()
    return {
        'CART_COUNT' : cart_items
    }