from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from decimal import Decimal
from .models import Product, Category  # <-- ОСЬ ТУТ МИ ДОДАЛИ Category
from .cart import Cart


def index(request):
    categories = Category.objects.all()
    return render(request, 'shop/index.html', {'categories': categories})


def cart_add(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)

    return redirect(f"{reverse('index')}#menu")


def cart_detail(request):
    cart = Cart(request)
    cart_items = []
    total_price = Decimal('0.00')

    for item_id, item_data in cart.cart.items():
        product = get_object_or_404(Product, id=item_id)
        total = Decimal(item_data['price']) * item_data['quantity']
        total_price += total
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'total': total
        })

    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})

# ... твій попередній код (index, cart_add, cart_detail) залишається тут ...

# НОВІ ФУНКЦІЇ ДЛЯ КОШИКА:

def cart_add_one(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail') # Залишаємось у кошику

def cart_remove_one(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.decrement(product=product)
    return redirect('cart_detail')

def cart_remove(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product=product)
    return redirect('cart_detail')

def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect('cart_detail')