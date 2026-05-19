from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/<int:product_id>/', views.cart_add, name='cart_add'),
    path('cart/', views.cart_detail, name='cart_detail'),

    # Нові шляхи для кнопок +, -, видалити і очистити
    path('cart/add-one/<int:product_id>/', views.cart_add_one, name='cart_add_one'),
    path('cart/remove-one/<int:product_id>/', views.cart_remove_one, name='cart_remove_one'),
    path('cart/remove/<int:product_id>/', views.cart_remove, name='cart_remove'),
    path('cart/clear/', views.cart_clear, name='cart_clear'),
]