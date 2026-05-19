from django.shortcuts import render
from .models import Product  # Підключаємо таблицю товарів


def index(request):
    # Беремо всі товари, де стоїть галочка "В наявності"
    products = Product.objects.filter(is_available=True)

    # Передаємо їх у HTML-шаблон під іменем 'products'
    return render(request, 'shop/index.html', {'products': products})