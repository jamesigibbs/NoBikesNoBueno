# Generated by Django 3.2.1 on 2021-06-21 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_remove_product_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]