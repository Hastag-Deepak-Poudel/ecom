from .models import CartItem

# def add_to_cart(request, pk):
#     product = Product.objects.get(id=pk)
#     cart_item, created = CartItem.objects.get_or_create(product=product, user = request.user)
#     cart_item.quantity += 1
#     cart_item.save()
#     return redirect('shop:show_details',pk)


from django.db.models import Sum

def cart_item_count(request):
    total = 0

    if request.user.is_authenticated:
        total = (
            CartItem.objects
            .filter(user=request.user)
            .aggregate(total=Sum('quantity'))['total'] or 0
        )

    return {'total': total}