# Generated by Django 4.1.6 on 2023-02-11 17:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0024_alter_products_part_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
