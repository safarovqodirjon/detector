# Generated by Django 4.1.6 on 2023-02-11 15:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0021_remove_products_part_number2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filenames',
            old_name='model_name',
            new_name='filename',
        ),
    ]
