# Generated by Django 4.1.5 on 2023-01-29 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0012_alter_order_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='orderCompany',
            field=models.CharField(max_length=25, verbose_name='Firma'),
        ),
        migrations.AlterField(
            model_name='order',
            name='orderName',
            field=models.CharField(max_length=25, verbose_name='Produkt'),
        ),
    ]
