# Generated by Django 3.2.9 on 2023-06-22 08:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.PositiveBigIntegerField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('last_purchase', models.DateTimeField(default=django.utils.timezone.now, editable=False)),
            ],
        ),
    ]
