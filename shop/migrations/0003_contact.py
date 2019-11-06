# Generated by Django 2.2.1 on 2019-05-21 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20190514_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=1000)),
            ],
        ),
    ]