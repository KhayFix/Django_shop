import json
from datetime import datetime

from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect
from django.views import View
from django.http import JsonResponse

from .models import Product, Order, OrderItem, ShippingAddress, CouponDiscount
from .utils import ObjectDetailCheckoutCartMixin
from .forms import CouponForm


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
    """Обработка данных от cart.js и добавления их в корзину товаров.

    Получаем данные от cart.js ввиде json {'productId': '4', 'action': 'add'}
    """
    data = json.loads(request.body)
    product_id, action = data.get('productId'), data.get('action')

    customer = request.user.customer
    product = Product.objects.get(id=product_id)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    order_item, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        order_item.quantity += 1
    elif action == 'remove':
        order_item.quantity -= 1
    order_item.save()

    if order_item.quantity <= 0:
        order_item.delete()

    return JsonResponse('Добавленно', safe=False)


def process_order(request):
    """Получения данных из формы 'Информация о доставке' """
    data = json.loads(request.body)
    transaction_id = datetime.now().timestamp()
    total = int(data['user'].get('total'))

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)

        order.transaction_id = transaction_id

        if total == int(order.get_cart_total):  # перевод статуса корзины в True, тем самым мы убираем товары из нее.
            order.complete = True
        order.save()

        if order.shipping:
            ShippingAddress.objects.create(
                customer=customer,
                order=order,
                region=data['shipping'].get('state'),
                city=data['shipping'].get('city'),
                address=data['shipping'].get('address'),
                zipcode=data['shipping'].get('zipcode'),
            )
    else:
        print('Пользователь не авторизован')

    return JsonResponse('Данные получены', safe=False)


def get_coupon(request, code):
    try:
        coupon = CouponDiscount.objects.get(code=code)
        return coupon
    except ObjectDoesNotExist:
        messages.info(request, f"Купон {code} не существует.")


class AddCouponView(View):
    def post(self, *args, **kwargs):
        form = CouponForm(self.request.POST or None)

        if form.is_valid():
            try:
                code = form.cleaned_data.get('code')
                coupon = get_coupon(self.request, code)
                if coupon:
                    customer = self.request.user.customer
                    order = Order.objects.get(customer=customer, complete=False)
                    order.coupon = coupon
                    order.save()
                    messages.success(self.request, f"Купон {code} успешно добавлен.")
            except ObjectDoesNotExist:
                messages.info(self.request, "У вас нет активного заказа.")
            return redirect('checkout_url')
