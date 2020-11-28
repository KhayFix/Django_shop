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

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "Покупатель"
        verbose_name_plural = "Покупатели"


class Order(models.Model):
    customer = models.ForeignKey("Customer", verbose_name="Покупатель", on_delete=models.SET_NULL,
                                 null=True, blank=True)
    data_ordered = models.DateTimeField(auto_now_add=True, verbose_name="Дата заказа")
    complete = models.BooleanField(default=False, verbose_name="Статус корзины")
    transaction_id = models.CharField(max_length=100, verbose_name="ID транзакции")

    def __repr__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"


class Product(models.Model):
    name = models.CharField(verbose_name='Название товара', max_length=200, null=True)
    price = models.FloatField(verbose_name='Цена')
    # если товар цифровой, то его можно не отправлять(почтой), за это будет отвечать digital
    digital = models.BooleanField(default=False, blank=True, verbose_name="Цифровой товар")
    image = models.ImageField(verbose_name="Изображение", upload_to='image_product/')

    def __repr__(self):
        return self.name

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"


class OrderItem(models.Model):
    product = models.ForeignKey("Product", verbose_name="Товар", on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey("Order", verbose_name="Заказ", on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, verbose_name="Колличество", blank=True)
    data_added = models.DateTimeField(auto_now_add=True, verbose_name="Дата добавления")

    def __repr__(self):
        return f"{self.product.name}->{self.product.price}"

    class Meta:
        verbose_name = "Позиция заказа"
        verbose_name_plural = "Позиции заказа"


class ShippingAddress(models.Model):
    customer = models.ForeignKey("Customer", verbose_name="Покупатель",
                                 on_delete=models.SET_NULL, null=True, blank=True
                                 )
    order = models.ForeignKey("Order", verbose_name="Заказ", on_delete=models.SET_NULL, null=True, blank=True)
    region = models.CharField(max_length=200, verbose_name="Область")
    city = models.CharField(max_length=150, verbose_name="Город")
    address = models.CharField(max_length=150, verbose_name="Адрес")
    zipcode = models.CharField(max_length=150, verbose_name="Индекс")
    data_added = models.DateTimeField(auto_created=True, verbose_name="Дата заказа")

    def __repr__(self):
        return f"{self.zipcode}-{self.city}-{self.address}"

    class Meta:
        verbose_name = "Адрес доставки"
        verbose_name_plural = "Адреса доставки"
