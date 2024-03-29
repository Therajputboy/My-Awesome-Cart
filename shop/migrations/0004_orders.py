# Generated by Django 2.2.1 on 2019-06-11 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=121)),
                ('address', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=111)),
                ('zip_code', models.CharField(max_length=10)),
                ('state', models.CharField(max_length=111)),
            ],
        ),
    ]
