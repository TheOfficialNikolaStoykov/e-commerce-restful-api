# Generated by Django 5.1 on 2024-09-17 17:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shipping_app', '0004_delivery_shipping_label_url'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='delivery',
            name='estimated_delivery_date',
        ),
    ]
