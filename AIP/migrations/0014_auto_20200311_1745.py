# Generated by Django 3.0.3 on 2020-03-11 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIP', '0013_auto_20200311_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='c_tot_score',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=5),
        ),
    ]
