# Generated by Django 5.0.3 on 2024-03-19 17:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conf', '0007_product_cart'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
