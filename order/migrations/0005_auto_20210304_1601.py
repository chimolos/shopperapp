# Generated by Django 3.1.7 on 2021-03-04 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0004_auto_20210304_1246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_placed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='orderproduct',
            name='order_placed',
            field=models.BooleanField(default=False, editable=False),
        ),
        migrations.AlterField(
            model_name='shopcart',
            name='order_placed',
            field=models.BooleanField(default=False, editable=False),
        ),
    ]
