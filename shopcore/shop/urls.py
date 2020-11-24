from django.urls import path

from .views import ShopListView, cart, checkout

urlpatterns = [
    path('', ShopListView.as_view(), name='shop_view_url'),
    path('cart/', cart, name='cart_url'),
    path('checkout/', checkout, name='checkout_url'),
]