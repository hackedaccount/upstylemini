# Generated by Django 3.0.5 on 2020-05-17 01:32

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('salevelocity', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='salevelocity',
            name='datetime',
            field=models.DateTimeField(auto_created=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
