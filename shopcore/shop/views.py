from django.shortcuts import render
from django.views import View

from .models import Product


class ShopListView(View):
    template = 'shop/shop.html'

    def get(self, request):
        product = Product.objects.all()
        return render(request, self.template, context={"products": product})


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
