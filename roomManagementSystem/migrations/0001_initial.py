# Generated by Django 4.0.3 on 2022-03-12 05:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='rooms',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('room_name', models.CharField(max_length=30)),
                ('room_type', models.CharField(max_length=30)),
                ('room_image', models.ImageField(upload_to='images')),
                ('room_desc', models.CharField(max_length=30)),
            ],
        ),
    ]
