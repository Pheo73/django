# Generated by Django 5.0.2 on 2024-02-12 16:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nom_application', '0004_itinerary'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='arrival_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='departure_location',
            field=models.CharField(default='', max_length=255),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='departure_time',
            field=models.TimeField(default=datetime.time(0, 0)),
        ),
    ]
