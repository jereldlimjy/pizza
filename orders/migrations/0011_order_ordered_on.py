# Generated by Django 2.0.3 on 2020-04-08 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0010_auto_20200408_0756'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='ordered_on',
            field=models.DateField(default=None),
            preserve_default=False,
        ),
    ]
