# Generated by Django 4.1.5 on 2023-01-21 20:19

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('qr', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='orderFile',
            field=models.FileField(blank=True, null=True, upload_to='orders/', verbose_name='Plik'),
        ),
        migrations.AlterField(
            model_name='order',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
