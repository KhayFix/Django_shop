from django.db import models
from django.contrib.auth.models import User


# Create your models here.
# class User(models.Model):
#     user_name = models.CharField()
#     email = ''
#     first_name = ''
#     last_name = ''


class Customer(models.Model):
    user = models.OneToOneField(User, verbose_name="Пользователь", null=True, blank=True,
                                on_delete=models.CASCADE)
    name = models.CharField(max_length=150, verbose_name="Имя")
    email = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Order(models.Model):
    customer = models.ForeignKey("Customer", verbose_name="Покупатель", on_delete=models.SET_NULL,
                                 null=True, blank=True)
    coupon = models.ForeignKey('CouponDiscount', verbose_name="Скидочный купон", on_delete=models.SET_NULL,
                               blank=True, null=True)
    data_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    complete = models.BooleanField(default=False, verbose_name="Статус корзины")
    transaction_id = models.CharField(max_length=100, verbose_name="ID транзакции")

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        """Если товар не цифровой, то показываем форму для ввода адреса"""
        shipping = False
        order_item = self.orderitem_set.all()
        for data in order_item:
            if not data.product.digital:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        """Общая цена всех товаров в корзине"""
        order_items = self.orderitem_set.all()
        total = sum([item.get_total for item in order_items])
        if self.coupon:
            total -= self.coupon.amount
        return total

    @property
    def get_cart_items(self):
        """Общее колличество всех товаров в корзине"""
        order_items = self.orderitem_set.all()
        total = sum([item.quantity for item in order_items])
        return total

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=200, null=True)
    price = models.FloatField(verbose_name='Цена')
    # если товар цифровой, то его можно не отправлять(почтой), за это будет отвечать digital
    digital = models.BooleanField(default=False, blank=True, verbose_name="Цифровой товар")
    image = models.ImageField(verbose_name="Изображение", upload_to='image_product/',
                              default='placeholder.png', blank=True)

    def __str__(self):
        return self.name

    @property
    def image_url(self):
        try:
            url = self.image.url
        except ValueError:
            url = ' '
        return url

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class OrderItem(models.Model):
    product = models.ForeignKey("Product", verbose_name="Товар", on_delete=models.SET_NULL,
                                null=True)
    order = models.ForeignKey("Order", verbose_name="Заказ", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, verbose_name="Колличество", blank=True)
    data_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.product.name}->{self.product.price}"

    @property
    def get_total(self):
        """Общая цена каждого товара"""
        total = self.product.price * self.quantity
        return total

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"


class ShippingAddress(models.Model):
    customer = models.ForeignKey("Customer", verbose_name="Покупатель",
                                 on_delete=models.SET_NULL, null=True, blank=True
                                 )
    order = models.ForeignKey("Order", verbose_name="Заказ", on_delete=models.SET_NULL, null=True,
                              blank=True)
    region = models.CharField(max_length=200, verbose_name="Область", null=True)
    city = models.CharField(max_length=150, verbose_name="Город", null=True)
    address = models.CharField(max_length=150, verbose_name="Адрес", null=True)
    zipcode = models.CharField(max_length=150, verbose_name="Индекс", null=True)
    data_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")

    def __str__(self):
        return f"{self.zipcode}-{self.city}-{self.address}"

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"


class CouponDiscount(models.Model):
    code = models.CharField(max_length=20, verbose_name="Купон")
    amount = models.IntegerField(verbose_name='Сумма')

    def __str__(self):
        return self.code

    class Meta:
        verbose_name = "Скидочный купон"
        verbose_name_plural = "Скидочные купоны"
