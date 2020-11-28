# Generated by Django 3.1.1 on 2020-11-28 15:03

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shippingaddress',
            options={'verbose_name': 'Адрес доставки', 'verbose_name_plural': 'Адреса доставки'},
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='address',
            field=models.CharField(max_length=150, null=True, verbose_name='Адрес'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='city',
            field=models.CharField(max_length=150, null=True, verbose_name='Город'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='customer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.customer', verbose_name='Покупатель'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='data_added',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата заказа'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='order',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='shop.order', verbose_name='Заказ'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='region',
            field=models.CharField(max_length=200, null=True, verbose_name='Область'),
        ),
        migrations.AddField(
            model_name='shippingaddress',
            name='zipcode',
            field=models.CharField(max_length=150, null=True, verbose_name='Индекс'),
        ),
    ]
