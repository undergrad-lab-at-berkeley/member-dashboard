# Generated by Django 2.1.3 on 2018-11-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0014_auto_20181110_0419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='end_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Completed'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='start_date',
            field=models.DateField(blank=True, null=True, verbose_name='Date Started'),
        ),
    ]
