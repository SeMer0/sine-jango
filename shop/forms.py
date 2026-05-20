# shop/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Форма для реєстрації
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True, label="Email адреса")

    class Meta:
        model = User
        fields = ("username", "email")

# Форма для оформлення замовлення
class CheckoutForm(forms.Form):
    full_name = forms.CharField(label="ПІБ", widget=forms.TextInput(attrs={'placeholder': 'Іванов Іван'}))
    phone = forms.CharField(label="Телефон", widget=forms.TextInput(attrs={'placeholder': '+380...'}))
    address = forms.CharField(label="Адреса доставки", widget=forms.Textarea(attrs={'rows': 3}))