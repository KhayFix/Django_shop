from django.shortcuts import render
from django.views import View


class ShopListView(View):
    template = 'shop/shop.html'

    def get(self, request):
        return render(request, self.template, context={})


def cart(request):
    context = {}
    return render(request, 'shop/cart.html', context)


def checkout(request):
    context = {}
    return render(request, 'shop/checkout.html', context)
