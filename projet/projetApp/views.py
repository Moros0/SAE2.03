from django.shortcuts import render
from projetApp.models import Machine , Personnel

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