from django.shortcuts import redirect


def redirect_shop(request):
    """Редирект.

    Редирект бывает двух видов постоянный, 301(permanent=True)
    и временый 302 (по умолчанию).
    name='shop_view_url' наша вьюха в shop->urls.py
    """
    return redirect('shop_view_url',)
