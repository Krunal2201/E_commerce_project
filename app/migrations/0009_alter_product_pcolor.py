# Generated by Django 5.0.6 on 2025-03-29 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0008_product_prentprice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pcolor',
            field=models.TextField(max_length=20),
        ),
    ]
