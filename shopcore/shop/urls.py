from django.urls import path

from .views import *

urlpatterns = [
    path('', shop_view, name='shop_view_url'),
    path('cart/', cart, name='cart_url'),
    path('checkout/', checkout, name='checkout_url'),
]