# Generated by Django 4.1.5 on 2023-01-21 21:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0002_order_orderfile_alter_order_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='orderFile',
            new_name='file',
        ),
        migrations.AddField(
            model_name='order',
            name='url',
            field=models.UUIDField(default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
