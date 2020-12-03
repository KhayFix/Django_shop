from django.shortcuts import render


class ObjectDetailCheckoutCartMixin:
    model = None
    template = None

    def get(self, request):
        if request.user.is_authenticated:
            customer = request.user.customer
            order, created = self.model.objects.get_or_create(customer=customer, complete=False)
            items = order.orderitem_set.all()
        else:
            items = []
            order = {'get_cart_total': 0, 'get_cart_items': 0}

        context = {'items': items, self.model.__name__.lower(): order}
        return render(request, self.template, context)
