# Generated by Django 3.2.9 on 2023-06-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fd', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fixeddeposit',
            name='Date_of_Opening',
            field=models.DateField(null=True),
        ),
        migrations.AddField(
            model_name='fixeddeposit',
            name='period',
            field=models.PositiveIntegerField(default=0, editable=False),
        ),
        migrations.AlterField(
            model_name='fixeddeposit',
            name='maturity_date',
            field=models.DateField(null=True),
        ),
    ]
