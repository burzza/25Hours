# Generated by Django 4.0.3 on 2022-04-20 17:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('roomManagementSystem', '0015_alter_bookingdetails_rooms'),
    ]

    operations = [
        migrations.CreateModel(
            name='reservedDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('check_in', models.DateField(max_length=30)),
                ('check_out', models.DateField(max_length=30)),
                ('total_price', models.FloatField()),
                ('rooms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='roomManagementSystem.rooms')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='bookingDetails',
        ),
    ]