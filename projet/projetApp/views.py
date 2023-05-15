from django.shortcuts import render, redirect
from projetApp.models import Machine , Personnel
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .forms import LoginForm

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
            return redirect('index')  # Redirige vers une page d'accueil après la connexion
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'templates/html/login.html', {'form': LoginForm()})