# Generated by Django 4.0.3 on 2022-04-07 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('UserManagementSystem', '0009_alter_hotelowner_managers_hotelowner_is_customer_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='hotelOwner',
            new_name='hotel',
        ),
    ]
