# Generated by Django 2.1.3 on 2018-12-23 23:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0024_auto_20181209_2145'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lab',
            name='directors',
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=2500, null=True),
        ),
        migrations.AlterField(
            model_name='subgroup',
            name='description',
            field=models.TextField(max_length=2500, null=True),
        ),
    ]
