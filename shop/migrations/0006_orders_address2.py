# Generated by Django 2.2.1 on 2019-06-11 05:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_orders_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='address2',
            field=models.CharField(default='', max_length=200),
        ),
    ]
