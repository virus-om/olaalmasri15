# Generated by Django 4.0.4 on 2022-04-23 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vaccine', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vaccine',
            name='dead_line',
            field=models.DateTimeField(editable=False, verbose_name='date to take'),
        ),
    ]
