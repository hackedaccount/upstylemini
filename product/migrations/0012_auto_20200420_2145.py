# Generated by Django 3.0.5 on 2020-04-20 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0011_products_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='reviews',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
