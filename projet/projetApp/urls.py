from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('machine/' , views.liste_machine_view , name = 'machine'),
    path('personnel/' , views.liste_personnel_view , name = 'personnel'),
    path('login/', views.login_view, name='login'),
    path('compte/', views.compte_view, name='compte'),
    path('create_machine/', views.create_machine_view, name='create_machine'),
    path('create_personnel/', views.create_personnel_view, name='create_personnel'),

]