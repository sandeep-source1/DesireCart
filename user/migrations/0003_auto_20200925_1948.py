# Generated by Django 3.1 on 2020-09-26 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='cart',
            name='status',
            field=models.CharField(default='status not available', max_length=30),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Order',
        ),
    ]