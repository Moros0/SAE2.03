from django import forms
from .models import Machine, Personnel, Reseau

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['etat', 'nom', 'adresse_ip', 'masque', 'reseau_assoc', 'personnel_assoc', 'maintenance_date', 'mach']

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = ['nom','prenom','id','machine_assoc']

class ReseauForm(forms.ModelForm):
    class Meta:
        model = Reseau
        fields = ['nom', 'adresse_ip', 'masque']