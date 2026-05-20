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
# shop/forms.py

class CheckoutForm(forms.Form):
    full_name = forms.CharField(
        label="ПІБ",
        widget=forms.TextInput(attrs={'placeholder': 'Іванов Іван'})
    )
    phone = forms.CharField(
        label="Телефон",
        widget=forms.TextInput(attrs={'placeholder': '+380...'})
    )

    # Замість одного поля address додаємо деталі:
    street = forms.CharField(
        label="Вулиця",
        widget=forms.TextInput(attrs={'placeholder': 'напр. Лесі Українки'})
    )
    house_number = forms.CharField(
        label="Будинок",
        widget=forms.TextInput(attrs={'placeholder': '№ будинку'})
    )
    apartment = forms.CharField(
        label="Квартира/Офіс (необов'язково)",
        required=False,  # Це поле не обов'язкове
        widget=forms.TextInput(attrs={'placeholder': '№ кв/офісу'})
    )
    comment = forms.CharField(
        label="Коментар до замовлення",
        required=False,
        widget=forms.Textarea(attrs={'rows': 2, 'placeholder': 'Додаткова інформація для кур\'єра...'})
    )