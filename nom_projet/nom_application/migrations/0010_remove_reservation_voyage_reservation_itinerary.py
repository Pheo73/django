# Generated by Django 5.0.2 on 2024-02-28 10:01

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nom_application', '0009_alter_itinerary_transport_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='voyage',
        ),
        migrations.AddField(
            model_name='reservation',
            name='itinerary',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='nom_application.itinerary'),
        ),
    ]