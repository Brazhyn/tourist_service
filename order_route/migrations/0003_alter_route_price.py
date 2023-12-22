# Generated by Django 4.1.7 on 2023-12-04 13:16

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order_route', '0002_route_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='route',
            name='price',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(0)]),
        ),
    ]