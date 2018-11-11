# Generated by Django 2.1.3 on 2018-11-09 22:25

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('dashboard', '0004_auto_20181109_0549'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='github',
        ),
        migrations.RemoveField(
            model_name='member',
            name='linkedin',
        ),
        migrations.RemoveField(
            model_name='member',
            name='website',
        ),
        migrations.AddField(
            model_name='member',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]