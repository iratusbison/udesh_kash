# Generated by Django 3.2.9 on 2023-07-11 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_management', '0002_profile_supply'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='role',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
