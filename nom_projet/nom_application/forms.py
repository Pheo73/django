from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import Voyage, Itinerary, Reservation, User, Hebergement

class InscriptionForm(UserCreationForm):
    email = forms.EmailField(label='Adresse email')

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'username': 'Nom d\'utilisateur',
            'password1': 'Mot de passe',
            'password2': 'Confirmer le mot de passe',
        }
        error_messages = {
            'username': {
                'unique': 'Ce nom d\'utilisateur est déjà pris.',
            },
            'email': {
                'unique': 'Cette adresse email est déjà enregistrée.',
            },
        }

class ConnexionForm(AuthenticationForm):
    pass

class VoyageForm(forms.ModelForm):
    class Meta:
        model = Voyage
        fields = ['depart', 'destination', 'date_depart']
        labels = {
            'depart': 'Lieu de départ',
            'destination': 'Destination',
            'date_depart': 'Date de départ',
        }

class ItineraryForm(forms.ModelForm):
    class Meta:
        model = Itinerary
        fields = ['departure_location', 'destination', 'date', 'departure_time', 'arrival_time', 'number_of_seats', 'price', 'transport_type']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['itinerary']
        labels = {
            'itinerary': 'Voyage',
        }

class HebergementForm(forms.ModelForm):
    class Meta:
        model = Hebergement
        fields = ['nom', 'adresse', 'prix']
