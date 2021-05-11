# Generated by Django 3.2 on 2021-05-07 20:35

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartitem',
            name='quantity',
            field=models.IntegerField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
