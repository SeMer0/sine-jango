from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from decimal import Decimal
from .models import Product, Category, Order, OrderItem  # Додали Order, OrderItem
from .cart import Cart
from django.contrib.auth import logout, login
from django.contrib.auth.forms import UserCreationForm
from .forms import RegisterForm, CheckoutForm  # Додали CheckoutForm


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
        total = Decimal(str(item_data['price'])) * item_data['quantity']
        total_price += total
        cart_items.append({
            'product': product,
            'quantity': item_data['quantity'],
            'total': total
        })

    return render(request, 'shop/cart_detail.html', {'cart_items': cart_items, 'total_price': total_price})


def cart_add_one(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.add(product=product)
    return redirect('cart_detail')


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


def checkout(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = CheckoutForm(request.POST)
        if form.is_valid():
            # Рахуємо загальну суму
            total_amount = sum(Decimal(str(item['price'])) * item['quantity'] for item in cart.cart.values())

            # Створюємо замовлення
            order = Order.objects.create(
                user=request.user if request.user.is_authenticated else None,
                full_name=form.cleaned_data['full_name'],
                phone=form.cleaned_data['phone'],
                address=form.cleaned_data['address'],
                total_price=total_amount
            )

            # Створюємо записи товарів у замовленні
            for item_id, item_data in cart.cart.items():
                product = Product.objects.get(id=item_id)
                OrderItem.objects.create(
                    order=order,
                    product=product,
                    quantity=item_data['quantity'],
                    price=Decimal(str(item_data['price']))
                )

            cart.clear()
            return render(request, 'shop/checkout_success.html', {'order': order})
    else:
        form = CheckoutForm()
    return render(request, 'shop/checkout.html', {'form': form})


def profile(request):
    return render(request, 'shop/profile.html')


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = RegisterForm()
    return render(request, 'shop/register.html', {'form': form})