from django.shortcuts import render
from django.views import View

from .models import Product, Order
from .utils import ObjectDetailCheckoutCartMixin


class ShopListView(View):
    template = 'shop/shop.html'

    def get(self, request):
        product = Product.objects.all()
        return render(request, self.template, context={"products": product})


class Cart(ObjectDetailCheckoutCartMixin, View):
    model = Order
    template = 'shop/cart.html'


class Checkout(ObjectDetailCheckoutCartMixin, View):
    model = Order
    template = 'shop/checkout.html'
