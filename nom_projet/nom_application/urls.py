
from django.urls import path
from .views import index,inscription, connexion,deconnexion,create_itinerary,dashboard,liste_itineraires,ajouter_itineraire,supprimer_itineraire,choisir_itineraire,reserved_itineraries,delete_reservation,create_hebergement,liste_hebergement,choisir_hebergement,supprimer_hebergement

urlpatterns = [
    path("", index, name="index"),
    path('inscription/', inscription, name='inscription'),
    path('connexion/', connexion, name='connexion'),
    path('deconnexion/', deconnexion, name='deconnexion'),
    path('create_itinerary/', create_itinerary, name='create_itinerary'),
    path('dashboard/', dashboard, name='dashboard'),
    path('liste_itineraires/', liste_itineraires, name='liste_itineraires'),
    path('ajouter_itineraire/<int:itinerary_id>/', ajouter_itineraire, name='ajouter_itineraire'),
    path('supprimer_itineraire/<int:itinerary_id>/', supprimer_itineraire, name='supprimer_itineraire'),
    path('supprimer_hebergement/<int:hebergement_id>/', supprimer_hebergement, name='supprimer_hebergement'),
    path('choisir_itineraire/<int:itinerary_id>/', choisir_itineraire, name='choisir_itineraire'),
    path('choisir_hebergement/<int:hebergement_id>/', choisir_hebergement, name='choisir_hebergement'),
    path('reserved_itineraries/', reserved_itineraries, name='reserved_itineraries'),
    path('delete_reservation/<int:reservation_id>/', delete_reservation, name='delete_reservation'),
    path('create_hebergement/', create_hebergement, name='create_hebergement'),
    path('liste_hebergement/', liste_hebergement, name='liste_hebergement'),

]