# Generated by Django 3.2.9 on 2023-06-22 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resource', '0002_product_total_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='total_price',
            field=models.DecimalField(decimal_places=2, editable=False, max_digits=10, null=True),
        ),
    ]
