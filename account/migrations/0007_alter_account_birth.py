# Generated by Django 4.0.4 on 2022-04-25 02:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0006_account_birth'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birth',
            field=models.DateField(default=datetime.datetime(2022, 4, 25, 5, 26, 38, 613818), null=True, verbose_name='birth'),
        ),
    ]
