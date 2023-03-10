# Generated by Django 4.1.6 on 2023-02-10 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0008_delete_myuploadfile_rename_document_document_files_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_number', models.CharField(max_length=255)),
                ('part_number2', models.CharField(max_length=255)),
                ('part_number3', models.CharField(max_length=255)),
                ('part_number4', models.CharField(max_length=255)),
                ('dealer_name', models.CharField(max_length=50)),
                ('price', models.DecimalField(decimal_places=4, max_digits=10)),
                ('description', models.TextField(blank=True, null=True)),
                ('on_stock', models.IntegerField(blank=True, null=True)),
                ('delivery', models.IntegerField(blank=True, null=True)),
            ],
        ),
    ]
