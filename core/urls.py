from django.contrib import admin
from django.urls import path
from shop.views import home  # <-- Імпортуємо нашу функцію з shop

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),  # <-- Порожній шлях '' означає головну сторінку
]