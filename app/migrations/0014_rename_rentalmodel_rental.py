# Generated by Django 5.0.6 on 2025-04-13 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0013_rentalmodel_booking_date_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='rentalmodel',
            new_name='rental',
        ),
    ]
