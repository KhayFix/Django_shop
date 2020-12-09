from django.urls import path

from .views import ShopListView, Cart, Checkout, update_item, process_order

urlpatterns = [
    path('', ShopListView.as_view(), name='shop_view_url'),
    path('cart/', Cart.as_view(), name='cart_url'),
    path('checkout/', Checkout.as_view(), name='checkout_url'),

    path('update-item/', update_item, name='update_item_url'),
    path('process-order/', process_order, name='process_order_url'),
]