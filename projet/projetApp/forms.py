from django import forms
from .models import Machine, Personnel

class LoginForm(forms.Form):
    username = forms.CharField(label='Nom d\'utilisateur')
    password = forms.CharField(label='Mot de passe', widget=forms.PasswordInput)

class MachineForm(forms.ModelForm):
    class Meta:
        model = Machine
        fields = ['nom', 'maintenance_date', 'mach']

class PersonnelForm(forms.ModelForm):
    class Meta:
        model = Personnel
        fields = '__all__'