# Generated by Django 5.0.6 on 2024-06-24 14:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0006_product_content_uz_product_name_uz'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='content_en',
        ),
        migrations.RemoveField(
            model_name='product',
            name='name_en',
        ),
    ]
