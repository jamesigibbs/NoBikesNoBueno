# Generated by Django 3.2.1 on 2021-06-21 22:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0006_remove_product_size'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='image_url',
        ),
    ]