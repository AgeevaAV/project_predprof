from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import CartItem, Order

from catalog.models import Catalog

from django.utils import timezone
from catalog.models import BuyBox
from datetime import date

def product_list(request):
    products = Catalog.objects.all()
    return render(request, 'catalog/catalog.html', {'products': products})

@login_required
def add_to_cart(request, product_id, product_breakfast_or_lunch):
    product = get_object_or_404(Catalog, id=product_id)

    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product,
        defaults={'quantity': 1},
        breakfast_or_lunch1 = product_breakfast_or_lunch,
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    return redirect('menu')

@login_required
def cart_view(request):
    cart_items = CartItem.objects.filter(user=request.user)
    
    total = 0
    for item in cart_items:
        total += item.product.price * item.quantity

    context = {
        'title':'Оплата',
        'cart_items': cart_items,
        'total': total
    }
    
    return render(request, 'orders/order.html', context)


@login_required
def increase_item(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    item.quantity += 1
    item.save()
    return redirect('cart_view')

@login_required
def decrease_item(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    if item.quantity > 1:
        item.quantity -= 1  
        item.save()
    else:
        item.delete()  
    return redirect('cart_view')
@login_required
def remove_from_cart(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    item.delete()
    return redirect('cart_view')

@login_required
def update_quantity(request, item_id):
    item = get_object_or_404(CartItem, id=item_id, user=request.user)
    if request.method == 'POST':
        quantity = int(request.POST.get('quantity', 1))
        if quantity > 0:
            item.quantity = quantity
            item.save()
        else:
            item.delete()
    return redirect('cart_view')
@login_required
def remove_item(request, item_id):
    item = CartItem.objects.get(id=item_id, user=request.user)
    item.delete()  
    return redirect('cart_view')


def add_to_order(request):
    cart_items = CartItem.objects.filter(user=request.user)
    #оплата
    if not(BuyBox.objects.filter(user_name = request.user).exists()):
        for cart in cart_items:
            total = cart.quantity * cart.product.price
            Order.objects.create(
                structure = cart.product.name,
                priceAll = total,
                count1 = cart.quantity,
                breakfast_or_lunch = cart.breakfast_or_lunch1,
                user_name = request.user,
                created_at = timezone.now()
            )
        cart_items.delete()
    elif not(BuyBox.objects.filter(user_name = request.user, end_box__date__gt=date.today()).exists()):
        b1 = BuyBox.objects.get(user_name = request.user)
        b1.delete()
        for cart in cart_items:
            total = cart.quantity * cart.product.price
            Order.objects.create(
                structure = cart.product.name,
                priceAll = total,
                count1 = cart.quantity,
                breakfast_or_lunch = cart.breakfast_or_lunch1,
                user_name = request.user,
                created_at = timezone.now()
            )
        cart_items.delete()
    else:
        box2 = BuyBox.objects.get(user_name = request.user)
        
        Chart_use_lunch = box2.created_at_lunch
        Chart_use_breakfast = box2.created_at_breakfast

        if Chart_use_lunch == timezone.localdate() and Chart_use_breakfast == timezone.localdate():
            for cart in cart_items:
                total = cart.quantity * cart.product.price
                Order.objects.create(
                    structure = cart.product.name,
                    priceAll = total,
                    count1 = cart.quantity,
                    breakfast_or_lunch = cart.breakfast_or_lunch1,
                    user_name = request.user,
                    created_at = timezone.now()
                )
            cart_items.delete()
        elif Chart_use_lunch == timezone.localdate() and Chart_use_breakfast != timezone.localdate():
            check = 1
            for cart in cart_items:
                if cart.breakfast_or_lunch1 == 'завтрак':
                    total = (cart.quantity - check) * cart.product.price
                    check = 0
                else:
                    total = cart.quantity * cart.product.price
                Order.objects.create(
                    structure = cart.product.name,
                    priceAll = total,
                    count1 = cart.quantity,
                    breakfast_or_lunch = cart.breakfast_or_lunch1,
                    user_name = request.user,
                    created_at = timezone.now()
                )
            cart_items.delete()
            if check == 0:
                box2.created_at_breakfast = timezone.localdate()
                box2.save()

        elif Chart_use_lunch != timezone.localdate() and Chart_use_breakfast == timezone.localdate():
            check = 1
            for cart in cart_items:
                if cart.breakfast_or_lunch1 == 'обед':
                    total = (cart.quantity - check) * cart.product.price
                    check = 0
                else:
                    total = cart.quantity * cart.product.price
                Order.objects.create(
                    structure = cart.product.name,
                    priceAll = total,
                    count1 = cart.quantity,
                    breakfast_or_lunch = cart.breakfast_or_lunch1,
                    user_name = request.user,
                    created_at = timezone.now()
                )
            cart_items.delete()
            if check == 0:
                box2.created_at_lunch = timezone.localdate()
                box2.save()
        
        elif Chart_use_lunch != timezone.localdate() and Chart_use_breakfast != timezone.localdate():
            check1 = 1
            check2 = 1
            for cart in cart_items:
                if cart.breakfast_or_lunch1 == 'завтрак':
                    total = (cart.quantity - check1) * cart.product.price
                    check1 = 0
                elif cart.breakfast_or_lunch1 == 'обед':
                    total = (cart.quantity - check2) * cart.product.price
                    check2 = 0
                else:
                    total = cart.quantity * cart.product.price
                Order.objects.create(
                    structure = cart.product.name,
                    priceAll = total,
                    count1 = cart.quantity,
                    breakfast_or_lunch = cart.breakfast_or_lunch1,
                    user_name = request.user,
                    created_at = timezone.now()
                )
            cart_items.delete()
            if check1 == 0:
                box2.created_at_lunch = timezone.localdate()
            if check2 == 0:
                box2.created_at_breakfast = timezone.localdate()
            box2.save()
    return redirect('cart_view')