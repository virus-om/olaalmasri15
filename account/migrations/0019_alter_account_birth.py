# Generated by Django 4.0.4 on 2022-05-14 00:07

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0018_alter_account_age_in_days'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birth',
            field=models.DateField(default=datetime.date(2022, 5, 14), null=True, verbose_name='birth'),
        ),
    ]
