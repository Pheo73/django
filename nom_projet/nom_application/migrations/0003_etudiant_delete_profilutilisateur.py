# Generated by Django 5.0.2 on 2024-02-12 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nom_application', '0002_commentaire_hebergement_profilutilisateur_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Etudiant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=250)),
                ('prenom', models.CharField(max_length=250)),
                ('tel', models.CharField(max_length=15)),
                ('mail', models.EmailField(max_length=254)),
                ('date_naissance', models.DateField()),
                ('lieu_naissance', models.CharField(max_length=100)),
                ('adresse_rue', models.CharField(max_length=255)),
                ('adresse_ville', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='ProfilUtilisateur',
        ),
    ]
