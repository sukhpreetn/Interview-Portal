# Generated by Django 3.0.4 on 2020-03-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIP', '0004_auto_20200304_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='no_times_anwered_correctly',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='no_times_anwered_incorrectly',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='no_times_ques_served',
            field=models.IntegerField(default=0),
        ),
    ]
