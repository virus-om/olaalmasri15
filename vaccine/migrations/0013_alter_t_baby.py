# Generated by Django 4.0.4 on 2022-05-11 23:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0011_alter_account_address_and_more'),
        ('vaccine', '0012_t'),
    ]

    operations = [
        migrations.AlterField(
            model_name='t',
            name='baby',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account'),
        ),
    ]