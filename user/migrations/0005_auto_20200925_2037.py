# Generated by Django 3.1 on 2020-09-26 03:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_cart_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='delivered',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='cart',
            name='Datetime',
            field=models.DateTimeField(default=datetime.datetime(2020, 9, 25, 20, 37, 51, 161846)),
        ),
    ]
