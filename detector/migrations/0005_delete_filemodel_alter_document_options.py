# Generated by Django 4.1.6 on 2023-02-05 12:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0004_document'),
    ]

    operations = [
        migrations.DeleteModel(
            name='FileModel',
        ),
        migrations.AlterModelOptions(
            name='document',
            options={'verbose_name': 'Document', 'verbose_name_plural': 'Documents'},
        ),
    ]