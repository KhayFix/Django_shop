from django.shortcuts import render
from django.views import View

from .models import Product, Order


class ShopListView(View):
    template = 'shop/shop.html'

    def get(self, request):
        product = Product.objects.all()
        return render(request, self.template, context={"products": product})


def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}

    context = {'items': items, 'order': order}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
