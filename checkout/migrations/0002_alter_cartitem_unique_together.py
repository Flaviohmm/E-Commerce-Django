# Generated by Django 3.2.9 on 2022-01-03 12:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='cartitem',
            unique_together={('cart_key', 'product')},
        ),
    ]