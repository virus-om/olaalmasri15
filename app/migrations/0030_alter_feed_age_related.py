# Generated by Django 4.0.4 on 2022-08-09 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0029_alter_treatment_treat_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='age_related',
            field=models.CharField(default=1, max_length=10, verbose_name='age related (in months)'),
        ),
    ]
