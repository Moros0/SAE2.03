from django.shortcuts import render, redirect
from projetApp.models import Machine , Personnel
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, MachineForm, PersonnelForm

# Create your views here.

def index(request):
    return render(request, 'templates/index.html')

def liste_machine_view(request):
    machine = Machine.objects.all()
    context = {'machine' : machine}
    return render(request , 'templates/html/liste_machine.html' , context)

def liste_personnel_view(request):
    personnel = Personnel.objects.all()
    context = {'personnel' : personnel}
    return render(request , 'templates/html/liste_personnel.html' , context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')    # Redirige vers la page d'accueil après la connexion
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'templates/html/login.html', {'form': LoginForm()})

@login_required
def compte_view(request):
    user = request.user
    return render(request, 'templates/html/compte.html', {'user': user})

def create_machine_view(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            machine = form.save()   # Enregistre le modèle dans la base de données
            return redirect('machine_detail', pk=machine.pk)   # Redirige vers la nouvelle page
    else:
        form = MachineForm()
    
    return render(request, 'create_machine.html', {'form': form})

def create_personnel_view(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            personnel = form.save()   # Enregistre le modèle dans la base de données
            return redirect('Personnel_detail', pk=personnel.pk)   # Redirige vers la nouvelle page
    else:
        form = PersonnelForm()
    
    return render(request, 'create_Personnel.html', {'form': form})