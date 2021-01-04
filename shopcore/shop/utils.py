import json
from typing import Dict, List
from django.shortcuts import render
from django.db.models import ObjectDoesNotExist
from .models import Product
from .forms import CouponForm


class ObjectDetailCheckoutCartMixin:
    """Отображение товаров на главной странице, в корзине и в подтверждении товаров.

    products - поместите данные (Product.objects.all())
    для выводы товаров на главной странице.
    """
    model = None
    template = None
    products = None

    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = self.model.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
            cart_items = order.get_cart_items
        else:
            cookie_cart: dict = json.loads(request.COOKIES.get('cart', '{}'))  # {'1': {'quantity': 2}...}
            items, order = anonymous_user_cookie_cart(cookie_cart)
            cart_items = order['get_cart_items']
        coupon = CouponForm()
        context = {'products': self.products,
                   'items': items,
                   self.model.__name__.lower(): order,
                   'cart_items': cart_items,
                   'coupon': coupon,
                   }

        return render(request, self.template, context)


def anonymous_user_cookie_cart(cookie_cart: Dict) -> List[Dict] and Dict:
    """
    Используется для обработки данных из кук и
    генерации данных для рендеринга корзины анонимного пользователя.
    """
    items = []
    order = {'get_cart_total': 0, 'get_cart_items': 0, 'shipping': False}

    for key, value in cookie_cart.items():  # получили колл. товара в корзине через куки.
        try:
            products = Product.objects.get(id=key)
        except ObjectDoesNotExist as error:
            print(error)  # TODO тут должна быть запись в логи.
        else:
            order['get_cart_items'] += value.get('quantity')
            total = (products.price * value.get('quantity'))
            order['get_cart_total'] += total
            # используем для рендеринга корзины для анонимного пользователя
            item = {
                'product': {
                    'id': products.id,
                    'name': products.name,
                    'price': products.price,
                    'image_url': products.image_url, },
                'quantity': value.get('quantity'),
                'get_total': total,
            }
            items.append(item)

            if not products.digital:
                order['shipping'] = True

    return items, order
