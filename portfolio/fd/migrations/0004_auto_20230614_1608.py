# Generated by Django 3.2.9 on 2023-06-14 10:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0003_remove_fixeddeposit_period'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixeddeposit',
            name='maturity_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='fixeddeposit',
            name='maturity_plus_principal_amount',
            field=models.DecimalField(decimal_places=2, max_digits=10, null=True),
        ),
    ]
