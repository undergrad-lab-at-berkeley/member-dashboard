# Generated by Django 2.1.3 on 2018-11-10 04:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0012_auto_20181110_0412'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='github',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='linkedin',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
    ]
