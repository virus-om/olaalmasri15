# Generated by Django 4.0.4 on 2022-04-23 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='birth',
            field=models.DateField(default=None, null=True, verbose_name='birth'),
        ),
    ]