# Generated by Django 4.1.6 on 2023-02-10 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('detector', '0012_alter_products_dealer_name_alter_products_on_stock_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dialer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='products',
            name='dealer_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='detector.dialer'),
        ),
    ]
