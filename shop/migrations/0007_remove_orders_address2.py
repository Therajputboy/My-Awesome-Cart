# Generated by Django 2.2.1 on 2019-06-11 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_orders_address2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orders',
            name='address2',
        ),
    ]
