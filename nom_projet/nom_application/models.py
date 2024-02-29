import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Etudiant(models.Model):
    nom = models.CharField(max_length=250)
    prenom = models.CharField(max_length=250)
    tel = models.CharField(max_length=15)
    mail = models.EmailField()
    date_naissance = models.DateField()
    lieu_naissance = models.CharField(max_length=100)
    adresse_rue = models.CharField(max_length=255)
    adresse_ville = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.prenom} {self.nom}"

class Voyage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    depart = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    date_depart = models.DateTimeField()

    def __str__(self):
        return f"{self.depart} à {self.destination} le {self.date_depart}"

class Commentaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    voyage = models.ForeignKey(Voyage, on_delete=models.CASCADE)
    texte = models.TextField()
    date_commentaire = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.user.username} sur le voyage {self.voyage}"

class Itinerary(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    departure_location = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
    date = models.DateField()
    departure_time = models.TimeField(default=datetime.time(0, 0))
    arrival_time = models.TimeField(default=datetime.time(0, 0))
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    number_of_seats = models.IntegerField(default=0)
    TRANSPORT_CHOICES = [
        ('voiture', 'Voiture'),
        ('train', 'Train'),
        ('avion', 'Avion'),
    ]
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES, default='train')

    def get_absolute_url(self):
        return reverse('detail_itineraire', args=[str(self.id)])

class Reservation(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    itinerary = models.ForeignKey(Itinerary, on_delete=models.CASCADE, null=True)  
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation de {self.user.username} pour le voyage {self.itinerary}"

class Hebergement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=100)
    adresse = models.CharField(max_length=255)
    prix = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    def get_absolute_url(self):
        return reverse('detail_hebergement', args=[str(self.id)])
    
class ReservationHebergement(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hebergement = models.ForeignKey(Hebergement, on_delete=models.CASCADE, null=True)  
    date_reservation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Réservation de {self.user.username} pour l'hebergement {self.hebergement}"
