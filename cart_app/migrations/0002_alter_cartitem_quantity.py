# Generated by Django 5.1 on 2024-09-07 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartitem',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
