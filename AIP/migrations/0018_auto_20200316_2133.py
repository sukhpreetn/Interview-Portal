# Generated by Django 3.0.3 on 2020-03-16 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AIP', '0017_quiz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='quiz',
            name='name',
        ),
        migrations.RemoveField(
            model_name='quiz',
            name='subject',
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_name',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='quiz',
            name='quiz_subject',
            field=models.CharField(default='', max_length=40),
        ),
    ]
