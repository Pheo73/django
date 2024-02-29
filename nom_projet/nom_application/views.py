from django.shortcuts import render, get_object_or_404,redirect
from .models import Etudiant, Reservation, Itinerary,Hebergement, ReservationHebergement
from django.contrib.auth import authenticate, login,logout
from .forms import InscriptionForm, ReservationForm,ItineraryForm,VoyageForm,HebergementForm
from django.contrib.auth.decorators import login_required,user_passes_test
from django.utils import timezone
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseForbidden
from django.urls import reverse
import logging

def index(request):
    etudiants = Etudiant.objects.all()
    
    context = {'etudiants': etudiants}
    
    return render(request, 'nom_application/base.html', context)

def inscription(request):
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = InscriptionForm()

    return render(request, 'nom_application/inscription.html', {'form': form})

def connexion(request):
    form = AuthenticationForm(request, data=request.POST or None)
    
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            pass

    return render(request, 'nom_application/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('index')

def is_admin(user):
    return user.is_superuser

@login_required
def create_reservation(request, voyage_id):
    voyage = Voyage.objects.get(pk=voyage_id)
    
    if request.method == 'POST':
        form = ReservationForm(request.POST)
        if form.is_valid():
            reservation = Reservation.objects.create(user=request.user, voyage=voyage)
            return render(request, 'nom_application/reservation_confirmation.html', {'reservation': reservation})
    else:
        form = ReservationForm()

    return render(request, 'nom_application/create_reservation.html', {'form': form, 'voyage': voyage})

@user_passes_test(is_admin)
def create_itinerary(request):
    if request.method == 'POST':
        form = ItineraryForm(request.POST)
        if form.is_valid():
            itinerary = form.save(commit=False)
            itinerary.user = request.user
            itinerary.save()
            return render(request, 'nom_application/itinerary_confirmation.html', {'itinerary': itinerary})
    else:
        form = ItineraryForm()

    return render(request, 'nom_application/create_itinerary.html', {'form': form})

def dashboard(request):
    return render(request, 'nom_application/dashboard.html')

def liste_itineraires(request):
    search_query = request.GET.get('search', '')

    itineraires = Itinerary.objects.filter(
        departure_location__icontains=search_query
    )

    context = {
        'itineraires': itineraires,
    }

    return render(request, 'nom_application/liste_itineraires.html', context)

@login_required
def ajouter_itineraire(request, itinerary_id):
    return redirect('liste_itineraires')

@user_passes_test(is_admin)
def supprimer_itineraire(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, pk=itinerary_id)
    itinerary.delete()
    return redirect('liste_itineraires')

@login_required
def choisir_itineraire(request, itinerary_id):
    itinerary = get_object_or_404(Itinerary, pk=itinerary_id)

    existing_reservation = Reservation.objects.filter(user=request.user, itinerary=itinerary).exists()

    if not existing_reservation:
        Reservation.objects.create(user=request.user, itinerary=itinerary)
        return render(request, 'nom_application/reservation_confirmation.html', {'itinerary': itinerary})
    else:
        return render(request, 'nom_application/itineraire_already_reserved.html', {'itinerary': itinerary})
def reserved_itineraries(request):
    reserved_itineraries = Itinerary.objects.filter(reservation__user=request.user)
    return render(request, 'nom_application/reserved_itineraries.html', {'reserved_itineraries': reserved_itineraries})

def delete_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)


    if request.method == 'POST':
        reservation.delete()
        return HttpResponseRedirect(reverse('reserved_itineraries'))

    return render(request, 'nom_application/delete_reservation.html', {'reservation': reservation})
        
@user_passes_test(is_admin)
def create_hebergement(request):
    if request.method == 'POST':
        form = HebergementForm(request.POST)
        if form.is_valid():
            hebergement = form.save(commit=False)
            hebergement.user = request.user
            hebergement.save()
            return render(request, 'nom_application/hebergement_confirmation.html', {'hebergement': hebergement})
    else:
        form = HebergementForm()

    return render(request, 'nom_application/create_hebergement.html', {'form': form})

@user_passes_test(is_admin)
def supprimer_hebergement(request, hebergement_id):
    hebergement = get_object_or_404(Hebergement, pk=hebergement_id)
    hebergement.delete()
    return redirect('liste_hebergement')

def liste_hebergement(request):
    search_query = request.GET.get('search', '')

    hebergements = Hebergement.objects.filter(
        nom__icontains=search_query
    )

    context = {
        'hebergements': hebergements,
    }

    return render(request, 'nom_application/liste_hebergement.html', context)

@login_required
def choisir_hebergement(request, hebergement_id):
    hebergement = get_object_or_404(Hebergement, pk=hebergement_id)

    existing_reservation = ReservationHebergement.objects.filter(user=request.user, hebergement=hebergement).exists()

    if not existing_reservation:
        ReservationHebergement.objects.create(user=request.user, hebergement=hebergement)
        return render(request, 'nom_application/reservation_confirmation_hebergement.html', {'hebergement': hebergement})
    else:
        return render(request, 'nom_application/hebergement_already_reserved.html', {'hebergement': hebergement})