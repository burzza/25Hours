# Generated by Django 4.0.3 on 2022-04-03 07:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomManagementSystem', '0006_rooms_room_number'),
    ]

    operations = [
        migrations.AddField(
            model_name='rooms',
            name='user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]