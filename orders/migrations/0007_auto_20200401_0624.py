# Generated by Django 2.0.3 on 2020-04-01 06:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200401_0612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='platter',
            old_name='price',
            new_name='price_large',
        ),
        migrations.RenameField(
            model_name='sub',
            old_name='price',
            new_name='price_large',
        ),
        migrations.RemoveField(
            model_name='platter',
            name='size',
        ),
        migrations.RemoveField(
            model_name='sub',
            name='size',
        ),
        migrations.AddField(
            model_name='platter',
            name='price_small',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sub',
            name='price_small',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
            preserve_default=False,
        ),
    ]
