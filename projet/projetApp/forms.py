from django import forms
from django.core.exceptions import ValidationError
from .models import Machine, Personnel

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = [  'nom', 'maintenance_date', 'mach']

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = [  'id', 'nom', 'prenom']

class AjoutMachineForm(forms.Form):
    nom = forms.CharField(required=True , label="Nome de la machine")

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError("Ereur de format pour le nom")
        return data