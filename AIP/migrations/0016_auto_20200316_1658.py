# Generated by Django 3.0.3 on 2020-03-16 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIP', '0015_result_c_attempt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='result',
            name='c_tot_score',
            field=models.IntegerField(default=0),
        ),
    ]