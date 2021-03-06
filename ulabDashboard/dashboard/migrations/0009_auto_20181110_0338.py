# Generated by Django 2.1.3 on 2018-11-10 03:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0008_auto_20181109_2303'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.AlterField(
            model_name='member',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='bio',
            field=models.TextField(blank=True, default='', max_length=300),
        ),
        migrations.AlterField(
            model_name='member',
            name='join_date',
            field=models.DateField(default=datetime.date.today, verbose_name='Date Joined'),
        ),
    ]
