# Generated by Django 3.2.9 on 2023-06-14 09:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FixedDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('account_holder', models.CharField(max_length=100)),
                ('principal_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=2, max_digits=5)),
                ('maturity_date', models.DateField()),
            ],
        ),
    ]
