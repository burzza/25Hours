# Generated by Django 4.0.3 on 2022-04-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roomManagementSystem', '0008_rooms_end_date_rooms_start_date_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoGallary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('multipleimages', models.FileField(blank=True, null=True, upload_to='gallaries')),
            ],
        ),
    ]
