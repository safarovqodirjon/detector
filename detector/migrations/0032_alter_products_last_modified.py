# Generated by Django 4.1.6 on 2023-02-19 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0031_alter_products_last_modified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='last_modified',
            field=models.DateTimeField(),
        ),
    ]
