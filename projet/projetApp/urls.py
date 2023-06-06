from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machine/' , views.liste_machine_view , name = 'machine'),
    path('personnel/' , views.liste_personnel_view , name = 'personnel'),
    path('reseau/' , views.liste_reseau_view , name = 'reseau'),
    path('login/', views.login_view, name='login'),
    path('compte/', views.compte_view, name='compte'),
    path('machine/<pk>', views.machine_detail_view, name='detail_machine'),
    path('personnel/<pk>', views.personnel_detail_view, name='detail_personnel'),
    path('reseau/<pk>', views.reseau_detail_view, name='detail_reseau'),
    path('ajout_machine/', views.ajout_machine_view, name='ajout_machine'),
    path('ajout_personnel/', views.ajout_personnel_view, name='ajout_personnel'),
    path('ajout_reseau/', views.ajout_reseau_view, name='ajout_reseau'),
    path('modifier_machine/<pk>', views.modifier_machine_view, name='modifier_machine'),
    path('modifier_personnel/<pk>', views.modifier_personnel_view, name='modifier_personnel'),
    path('modifier_reseau/<pk>', views.modifier_reseau_view, name='modifier_reseau'),
    path('supprimer_machine/<pk>', views.supprimer_machine_view, name='supprimer_machine'),
    path('supprimer_personnel/<pk>', views.supprimer_personnel_view, name='supprimer_personnel'),
    path('supprimer_reseau/<pk>', views.supprimer_reseau_view, name='supprimer_reseau'),
    path('recherche/', views.recherche_view, name='recherche'),

]