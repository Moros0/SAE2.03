from django.shortcuts import render, redirect, get_object_or_404
from .models import Machine , Personnel, Reseau
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm, MachineForm, PersonnelForm, ReseauForm, SearchForm
from django.db.models import Q 

# Create your views here.

def index(request):
    return render(request, 'templates/index.html')


def liste_machine_view(request):
    machine = Machine.objects.all()
    return render(request , 'templates/html/liste_machine.html' , {'machine' : machine})


def liste_personnel_view(request):
    personnel = Personnel.objects.all()
    return render(request , 'templates/html/liste_personnel.html' , {'personnel' : personnel})

def liste_reseau_view(request):
    reseau = Reseau.objects.all()
    return render(request , 'templates/html/liste_reseau.html' , {'reseau' : reseau})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            messages.error(request, 'Nom d\'utilisateur ou mot de passe incorrect.')
    return render(request, 'templates/html/login.html', {'form': LoginForm()})


@login_required
def compte_view(request):
    user = request.user
    if request.user.is_authenticated:
        return render(request, 'templates/html/compte.html', {'user': user})
    else:
        return render(request, 'templates/html/login.html', {'form': LoginForm()})


def machine_detail_view(request, pk):
    machine = get_object_or_404(Machine, id = pk)
    return render(request, 'templates/html/detail_machine.html', {'machine': machine})


def personnel_detail_view(request, pk):
    personnel = get_object_or_404(Personnel, id = pk)
    return render(request, 'templates/html/detail_personnel.html', {'personnel': personnel})

def reseau_detail_view(request, pk):
    reseau = get_object_or_404(Reseau, id = pk)
    return render(request, 'templates/html/detail_reseau.html', {'reseau': reseau})

def ajout_machine_view(request):
    if request.method == 'POST':
        form = MachineForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('machine')
    else:
        form = MachineForm()
    
    return render(request, 'templates/html/ajout_machine.html', {'form': form}) 

def ajout_personnel_view(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('personnel')
    else:
        form = PersonnelForm()
    
    return render(request, 'templates/html/ajout_personnel.html', {'form': form}) 

def ajout_reseau_view(request):
    if request.method == 'POST':
        form = ReseauForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('reseau')
    else:
        form = ReseauForm()
    
    return render(request, 'templates/html/ajout_reseau.html', {'form': form}) 

def modifier_machine_view(request, pk):
    instance = get_object_or_404(Machine, pk=pk)
    
    if request.method == 'POST':
        form = MachineForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('machine')
    else:
        form = MachineForm(instance=instance)
    
    return render(request, 'templates/html/modifier_machine.html', {'form': form})

def modifier_personnel_view(request, pk):
    instance = get_object_or_404(Personnel, pk=pk)
    
    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('personnel')
    else:
        form = PersonnelForm(instance=instance)
    
    return render(request, 'templates/html/modifier_personnel.html', {'form': form})

def modifier_reseau_view(request, pk):
    instance = get_object_or_404(Reseau, pk=pk)
    
    if request.method == 'POST':
        form = ReseauForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('reseau')
    else:
        form = ReseauForm(instance=instance)
    
    return render(request, 'templates/html/modifier_reseau.html', {'form': form})

def supprimer_machine_view(request, pk):
    instance = get_object_or_404(Machine, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        return redirect('machine')
    return render(request, 'templates/html/supprimer_machine.html', {'instance': instance})

def supprimer_personnel_view(request, pk):
    instance = get_object_or_404(Personnel, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        return redirect('personnel')
    return render(request, 'templates/html/supprimer_personnel.html', {'instance': instance})

def supprimer_reseau_view(request, pk):
    instance = get_object_or_404(Reseau, pk=pk)
    
    if request.method == 'POST':
        instance.delete()
        return redirect('reseau')
    return render(request, 'templates/html/supprimer_reseau.html', {'instance': instance})

def recherche_view(request):
    form = SearchForm(request.GET)
    results = {}

    if form.is_valid():
        search_query = form.cleaned_data['search_query']

        machine_results = Machine.objects.filter(
            Q(id__icontains=search_query) |
            Q(nom__icontains=search_query) |
            Q(adresse_ip__icontains=search_query) |
            Q(masque__icontains=search_query) |
            Q(maintenance_date__icontains=search_query) |
            Q(mach__icontains=search_query) |
            Q(etat__icontains=search_query)
        )
        results['Machine'] = machine_results

        personnel_results = Personnel.objects.filter(
            Q(id__icontains=search_query) |
            Q(nom__icontains=search_query) |
            Q(prenom__icontains=search_query) |
            Q(mail__icontains=search_query)
        )
        results['Personnel'] = personnel_results

        reseau_results = Reseau.objects.filter(
            Q(id__icontains=search_query) |
            Q(nom__icontains=search_query) |
            Q(adresse_ip__icontains=search_query) |
            Q(masque__icontains=search_query)
        )
        results['Reseau'] = reseau_results




    return render(request, 'templates/html/recherche.html', {'form': form, 'results': results})