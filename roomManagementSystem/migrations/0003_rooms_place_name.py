# Generated by Django 4.0.3 on 2022-03-20 01:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomManagementSystem', '0002_rename_room_name_rooms_hotel_name_rooms_room_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='place_name',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
    ]
