# Generated by Django 2.0.3 on 2020-04-01 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0007_auto_20200401_0624'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sub',
            name='price_small',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]
