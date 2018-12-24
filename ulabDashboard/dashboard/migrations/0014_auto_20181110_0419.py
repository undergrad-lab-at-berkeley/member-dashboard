# Generated by Django 2.1.3 on 2018-11-10 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0013_auto_20181110_0413'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lab',
            name='end_date',
            field=models.DateField(null=True, verbose_name='Date Completed'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='researchers',
            field=models.ManyToManyField(blank=True, related_name='researchers', to='dashboard.Member'),
        ),
        migrations.AlterField(
            model_name='lab',
            name='start_date',
            field=models.DateField(null=True, verbose_name='Date Started'),
        ),
    ]
