# Generated by Django 4.1.6 on 2023-02-05 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0002_alter_file_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='FileModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to='files/')),
            ],
        ),
        migrations.DeleteModel(
            name='File',
        ),
    ]
