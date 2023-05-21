from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machine/' , views.liste_machine_view , name = 'machine'),
    path('personnel/' , views.liste_personnel_view , name = 'personnel'),
    path('login/', views.login_view, name='login'),
    path('compte/', views.compte_view, name='compte'),
    path('machine/<pk>', views.machine_detail_view, name='machine_detail'),
    path('personnel/<pk>', views.personnel_detail_view, name='personnel_detail'),
    path('ajout_machine/', views.ajout_machine_view, name='ajout_machine'),
    path('ajout_personnel/', views.ajout_personnel_view, name='ajout_personnel'),
    path('modifier_machine/<pk>', views.modifier_machine_view, name='modifier_machine'),
    path('modifier_personnel/<pk>', views.modifier_personnel_view, name='modifier_personnel'),
    path('supprimer_machine/<pk>', views.supprimer_machine_view, name='supprimer_machine'),

]