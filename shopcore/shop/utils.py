from django.shortcuts import render


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
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}
            cart_items = order['get_cart_items']

        context = {'products': self.products,
                   'items': items,
                   self.model.__name__.lower(): order,
                   'cart_items': cart_items
                   }

        return render(request, self.template, context)
