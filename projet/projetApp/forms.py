from django import forms
from .models import Machine, Personnel, Reseau

class LoginForm(forms.Form):        #formulaire utilisé pour gérer la connexion
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class MachineForm(forms.ModelForm):     #formulaire utilisé pour tout ce qui touche au modele machine
    class Meta:
        model = Machine
        fields = ['etat', 'nom', 'adresse_ip', 'masque', 'reseau_assoc', 'personnel_assoc', 'maintenance_date', 'mach']

class PersonnelForm(forms.ModelForm):       #formulaire utilisé pour tout ce qui touche au modele personnel
    class Meta:
        model = Personnel
        fields = ['nom','prenom','id']

class ReseauForm(forms.ModelForm):      #formulaire utilisé pour tout ce qui touche au modele reseau
    class Meta:
        model = Reseau
        fields = ['nom', 'adresse_ip', 'masque']

class SearchForm(forms.Form):       #formulaire pour gérer la recherche depuis la page recherche
    search_query = forms.CharField(label='Recherche')