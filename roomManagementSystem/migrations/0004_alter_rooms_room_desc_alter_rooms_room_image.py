# Generated by Django 4.0.3 on 2022-03-20 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomManagementSystem', '0003_rooms_place_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rooms',
            name='room_desc',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='rooms',
            name='room_image',
            field=models.ImageField(upload_to=''),
        ),
    ]
