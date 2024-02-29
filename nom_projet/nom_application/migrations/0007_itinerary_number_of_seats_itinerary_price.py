# Generated by Django 5.0.2 on 2024-02-14 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nom_application', '0006_alter_itinerary_departure_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='itinerary',
            name='number_of_seats',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='itinerary',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
    ]