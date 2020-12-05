from django.views import View
from django.http import JsonResponse

from .models import Product, Order
from .utils import ObjectDetailCheckoutCartMixin


class ShopListView(ObjectDetailCheckoutCartMixin, View):
    model = Order
    template = 'shop/shop.html'
    products = Product.objects.all()

    # def get(self, request):
    #     if request.user.is_authenticated:
    #         customer = request.user.customer
    #         order = Order.objects.get(customer=customer).get_cart_items
    #     else:
    #         order = 0
    #
    #     product = Product.objects.all()
    #     return render(request, self.template, context={"products": product, "cart_items": order})


class Cart(ObjectDetailCheckoutCartMixin, View):
    model = Order
    template = 'shop/cart.html'


class Checkout(ObjectDetailCheckoutCartMixin, View):
    model = Order
    template = 'shop/checkout.html'


def update_item(request):
    return JsonResponse('Добавленно', safe=False)
