# Generated by Django 4.0.4 on 2022-08-04 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0019_alter_feed_food_name_alter_feed_food_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='food_type',
            field=models.CharField(choices=[('N_milk', 'Nmilk'), ('Fmilk', 'Fmilk'), ('water', 'water'), ('fruits', 'fruits'), ('vegetables', 'vegetables'), ('cyrbohedats', 'cyrbohedats'), ('cremy', 'cremy')], default='default type', max_length=25, null=True),
        ),
    ]
