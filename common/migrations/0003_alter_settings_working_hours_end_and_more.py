# Generated by Django 4.2 on 2024-06-24 15:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_alter_page_table_alter_settings_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='working_hours_end',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='settings',
            name='working_hours_start',
            field=models.IntegerField(),
        ),
    ]
